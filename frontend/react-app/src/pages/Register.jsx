import React, { useState } from "react";
import API from "../services/Api.jsx";
import { useNavigate } from "react-router-dom";

function Register() {
    const [email, setEmail] = useState(""); 
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleRegister = async () => {
        try {
            await API.post("/register", {
                email,
                password
            });
            navigate("/login")
        }
        catch (err) {
            alert(err.response?.data?.detail || "Registration failed");
        };
    }

    return (
        <div>
            <h2>Register</h2>   
            <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
            <input placeholder="Password" type="password" onChange={(e) => setPassword(e.target.value)} />
            <button onClick={handleRegister}>Register</button>
        </div>
    );
}

export default Register;
