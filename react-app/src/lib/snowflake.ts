import snowflake from "snowflake-sdk";
import fs from "fs";
import path from "path";

let connectionPool: snowflake.Connection | null = null;
let connectingPromise: Promise<snowflake.Connection> | null = null;

const SPCS_TOKEN_PATH = "/snowflake/session/token";

function readSpcsToken(): string | null {
  try {
    return fs.readFileSync(SPCS_TOKEN_PATH, "utf-8").trim();
  } catch {
    return null;
  }
}

function buildConnectionConfig(): snowflake.ConnectionOptions {
  const base: snowflake.ConnectionOptions = {
    account: process.env.SNOWFLAKE_ACCOUNT || process.env.SNOWFLAKE_HOST?.split(".")[0] || "",
    username: process.env.SNOWFLAKE_USER || "",
    warehouse: process.env.SNOWFLAKE_WAREHOUSE || "",
    database: process.env.SNOWFLAKE_DATABASE || "",
    role: process.env.SNOWFLAKE_ROLE || "",
  };

  if (process.env.SNOWFLAKE_HOST) {
    base.accessUrl = `https://${process.env.SNOWFLAKE_HOST}`;
  }

  const spcsToken = readSpcsToken();
  if (spcsToken) {
    return { ...base, authenticator: "OAUTH", token: spcsToken };
  }

  if (process.env.SNOWFLAKE_TOKEN) {
    return { ...base, authenticator: "OAUTH", token: process.env.SNOWFLAKE_TOKEN };
  }

  if (process.env.SNOWFLAKE_PASSWORD) {
    return { ...base, password: process.env.SNOWFLAKE_PASSWORD };
  }

  const keyPath = path.join(
    process.env.HOME || process.env.USERPROFILE || "",
    ".snowflake",
    "rsa_key.p8"
  );
  if (fs.existsSync(keyPath)) {
    return {
      ...base,
      authenticator: "SNOWFLAKE_JWT",
      privateKey: fs.readFileSync(keyPath, "utf-8"),
    };
  }

  return base;
}

function getConnection(): Promise<snowflake.Connection> {
  if (connectionPool && connectionPool.isUp()) {
    return Promise.resolve(connectionPool);
  }

  if (connectingPromise) {
    return connectingPromise;
  }

  connectingPromise = new Promise<snowflake.Connection>((resolve, reject) => {
    const conn = snowflake.createConnection(buildConnectionConfig());
    conn.connect((err) => {
      connectingPromise = null;
      if (err) {
        reject(err);
      } else {
        connectionPool = conn;
        resolve(conn);
      }
    });
  });

  return connectingPromise;
}

export async function executeQuery<T = Record<string, unknown>>(
  sql: string
): Promise<T[]> {
  const conn = await getConnection();
  return new Promise((resolve, reject) => {
    conn.execute({
      sqlText: sql,
      complete: (err, _stmt, rows) => {
        if (err) {
          reject(err);
        } else {
          resolve((rows || []) as T[]);
        }
      },
    });
  });
}
