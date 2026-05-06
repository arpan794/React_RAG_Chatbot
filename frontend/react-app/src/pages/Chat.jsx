import React, { useState } from "react";
import API from "../services/Api";


function chat() {
    const [question, setQuestion] = useState("");
    const [response, setResponse] = useState("");

    const askQuestion = async () => {
        try {
            const res = await API.post("/chat/chat", { question });
            setResponse(res.data.response);
        }
        catch (err) {
            alert(err.response?.data?.detail || "Chat failed");
        }
    }

    return (
        <div>
            <h2>Chat</h2>
            <input placeholder="Ask a question..." onChange={(e) => setQuestion(e.target.value)} />
            <button onClick={askQuestion}>Ask</button>

            {response && (  
                <div>
                    <h3>Response:</h3>
                    <p>{response}</p>
                </div>
            )}
        </div>

    )

}

export default chat;