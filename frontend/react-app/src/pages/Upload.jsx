import React, { useState } from "react";
import API from "../services/Api.jsx";

function Upload() {
    const [file, setfile] = useState(null);

    const handleUpload  = async () => {
        if (!file) {
            alert("Please select a file to upload");
            return;
        }

        try {
            const formData = new FormData();
            formData.append("file", file);

            // const token = localStorage.getItem("token");
           const res = await API.post("/upload/upload", formData)
            alert(res.data.message);

        } catch (err) {
            alert(err.response?.data?.detail || "Upload failed");
        }
    }
    return (
        <div>
            <h2>Upload</h2>
            <input type="file" onChange={(e) => setfile(e.target.files[0])} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    )
}

export default Upload;

