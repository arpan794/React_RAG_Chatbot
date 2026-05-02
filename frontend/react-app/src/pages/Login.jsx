import React, { useState } from "react";
import API from "../services/Api.jsx";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

const handleLogin = async () => {
  try {
    const res = await API.post("/login", {
      email,
      password
    });

    localStorage.setItem("token", res.data.access_token);
    navigate("/dashboard");

  } catch (err) {
    alert(err.response?.data?.detail || "Login failed");
  }
};

  return (
    <div>
      <h2>Login</h2>

      <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Password" type="password" onChange={(e) => setPassword(e.target.value)} />

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;
