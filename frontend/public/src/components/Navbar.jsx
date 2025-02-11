import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav style={styles.navbar}>
      <div style={styles.logo}>Event Manager</div>
      <ul style={styles.navLinks}>
        <li><Link to="/admin" style={styles.link}>Admin</Link></li>
        <li><Link to="/client" style={styles.link}>Client</Link></li>
        <li><Link to="/rsvp" style={styles.link}>RSVP</Link></li>
        <li><Link to="/login" style={styles.loginButton}>Login</Link></li>
      </ul>
    </nav>
  );
};

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "15px 30px",
    backgroundColor: "#333",
    color: "#fff",
  },
  logo: {
    fontSize: "1.5rem",
    fontWeight: "bold",
  },
  navLinks: {
    listStyle: "none",
    display: "flex",
    gap: "20px",
  },
  link: {
    color: "#fff",
    textDecoration: "none",
    fontSize: "1rem",
  },
  loginButton: {
    color: "#fff",
    backgroundColor: "#ff8800",
    padding: "8px 15px",
    borderRadius: "5px",
    textDecoration: "none",
  }
};

export default Navbar;
