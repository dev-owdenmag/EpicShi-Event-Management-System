import { useState } from "react";
import { api } from "../api/api";

const RSVPPage = () => {
  const [guestCode, setGuestCode] = useState("");
  const [status, setStatus] = useState("");

  const handleRSVP = async () => {
    try {
      await api.post("/rsvp/confirm", { guestCode, status });
      alert("RSVP confirmed!");
    } catch (error) {
      console.error("RSVP failed", error);
    }
  };

  return (
    <div style={{ background: "linear-gradient(to right, #cd7f32, #a52a2a, #fff)" }}>
      <h2>RSVP Confirmation</h2>
      <input type="text" placeholder="Enter Guest Code" onChange={(e) => setGuestCode(e.target.value)} />
      <button onClick={handleRSVP}>Confirm Attendance</button>
    </div>
  );
};

export default RSVPPage;
