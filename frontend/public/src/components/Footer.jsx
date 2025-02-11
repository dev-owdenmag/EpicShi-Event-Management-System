import React from "react";

const Footer = () => {
  return (
    <footer style={styles.footer}>
      <p>© {new Date().getFullYear()} Event Management System. All Rights Reserved.</p>
    </footer>
  );
};

const styles = {
  footer: {
    textAlign: "center",
    padding: "15px",
    backgroundColor: "#333",
    color: "#fff",
    marginTop: "20px",
  },
};

export default Footer;
