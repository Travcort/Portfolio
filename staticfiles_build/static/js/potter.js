document.addEventListener("DOMContentLoaded", function() {

    // The Refresh Button
    var refreshButton = document.getElementById("refresh");
    if(refreshButton) {
        refreshButton.addEventListener("click", function() {
            console.log("Refreshed!");
            location.reload();
        });
    }
    else {
        console.error("Refresh Button not found!");
    }

    // Resizing the textarea element in books.html and spells.html
    if (document.getElementById("text-area")) {
        var textarea = document.getElementById('text-area');
        textarea.style.height = "auto";
        textarea.style.height = (textarea.scrollHeight) + "px";
    }

    
});

