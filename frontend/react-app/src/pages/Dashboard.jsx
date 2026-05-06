import React, { useEffect, useState } from "react";
import API from "../services/Api.jsx";

function Dashboard() {
//   const [message, setMessage] = useState("");
//   const [email, setEmail] = useState("");
  
  const [profile, setProfile] = useState(null);
  const [error, setError] = useState(""); 
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");

        const res = await API.get("/auth/profile", {
          headers: { Authorization: `Bearer ${token}` }
        });

        // setMessage(res.data.message);
        // setEmail(res.data.email);

        setProfile(res.data);

      } catch (err) {
        console.log(err);
        setError("Unauthorized or Failed to load profile");
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

   return (
    <div>
      <h2>Dashboard</h2>

      {loading && <p>Loading...</p>}

      {!loading && error && (
        <p style={{ color: "red" }}>{error}</p>
      )}

      {!loading && !error && profile && (
        <>
          <p>{profile.message}</p>
          <p>{profile.email}</p>
        </>
      )}
    </div>
  );
}

export default Dashboard;