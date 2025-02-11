import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import AdminDashboard from "./pages/AdminDashboard";
import ClientDashboard from "./pages/ClientDashboard";
import Login from "./pages/Login";
import RSVP from "./pages/RSVP";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/client" element={<ClientDashboard />} />
        <Route path="/login" element={<Login />} />
        <Route path="/rsvp" element={<RSVP />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
