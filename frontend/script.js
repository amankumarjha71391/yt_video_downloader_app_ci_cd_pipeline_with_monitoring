document.querySelector("#downloadButton").addEventListener("click", async (event) => {
    event.preventDefault(); // Prevent the page from refreshing

    const urlInput = document.querySelector("#urlInput").value;

    if (!urlInput) {
        alert("Please enter a URL!");
        return;
    }

    const formData = new FormData();
    formData.append("url", urlInput);

    try {
        const response = await fetch("http://127.0.0.1:8000/download/", {
            method: "POST",
            body: formData,
        });

        // Check if the response status is OK (200)
        if (response.ok) {
            const result = await response.json();
            console.log(result);  // Log the result for debugging

            alert(result.message);

            // Ensure the result.path is correct
            if (result.path) {
                // Handle file download by creating a temporary download link
                const fileUrl = result.path; // This will work if FastAPI is already serving the file
                const a = document.createElement('a');
                a.href = fileUrl; // This will work if FastAPI is already serving the file
                a.download = result.path.split('/').pop(); // Set filename from the path
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);

                // Show success message
                const downloadMessage = document.querySelector("#downloadMessage");
                downloadMessage.classList.remove("hidden");
            }
        } else {
            const error = await response.json();
            alert(`Error: ${error.detail}`);
        }

    } catch (error) {
        console.error("Error:", error);
        alert("Download success.");
    }
});
