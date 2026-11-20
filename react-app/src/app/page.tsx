"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Header from "@/components/layout/Header";
import Sidebar, { type PageId } from "@/components/layout/Sidebar";
import OverviewPage from "@/components/overview/OverviewPage";
import ContactsPage from "@/components/contacts/ContactsPage";
import ActivityPage from "@/components/activity/ActivityPage";
import IntelligencePage from "@/components/intelligence/IntelligencePage";
import CrmTab from "@/components/crm/CrmTab";
import PrioritizationTab from "@/components/prioritization/PrioritizationTab";
import AlignmentTab from "@/components/alignment/AlignmentTab";
import DataArchitecturePage from "@/components/architecture/DataArchitecturePage";
import ToastContainer from "@/components/shared/Toast";
import Footer from "@/components/layout/Footer";

const pages: Record<PageId, React.ComponentType<{ onNavigate?: (page: PageId) => void }>> = {
  overview: OverviewPage,
  contacts: ContactsPage,
  activity: ActivityPage,
  intelligence: IntelligencePage,
  crm: CrmTab,
  prioritization: PrioritizationTab,
  alignment: AlignmentTab,
  architecture: DataArchitecturePage,
};

export default function Dashboard() {
  const [activePage, setActivePage] = useState<PageId>("overview");
  const ActiveComponent = pages[activePage];

  return (
    <div className="h-screen flex flex-col">
      <Header onNavigate={setActivePage} />
      <div className="flex flex-1 overflow-hidden">
        <Sidebar activePage={activePage} onNavigate={setActivePage} />
        <main className="flex-1 overflow-y-auto p-6">
          <div className="max-w-[1400px] mx-auto">
            <AnimatePresence mode="wait">
              <motion.div
                key={activePage}
                initial={{ opacity: 0, y: 8 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -8 }}
                transition={{ duration: 0.2 }}
              >
                <ActiveComponent onNavigate={setActivePage} />
              </motion.div>
            </AnimatePresence>
          </div>
        </main>
      </div>
      <Footer />
      <ToastContainer />
    </div>
  );
}
