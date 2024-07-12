document.addEventListener("DOMContentLoaded", function() {

    // The TypeWriter Effect on the Landing page heading
    if (document.getElementById("landing-header")) {
        function typeWriter() {
            let header = document.getElementById("landing-header");
            let charIndex = 0;
            const headerText = header.textContent;

            header.textContent = "";

            function type() {
                if (charIndex < headerText.length) {
                    header.textContent += headerText.charAt(charIndex);
                    charIndex ++;
                    setTimeout(type, 75);
                }
            }
            // Calling the Function
            type();
        }
        typeWriter();
    }

    // The Refresh Button
    if (document.getElementById("refresh")) {
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
    }

    // Resizing the textarea element in books.html and spells.html
    if (document.getElementById("text-area")) {
        var textarea = document.getElementById('text-area');
        textarea.style.height = "auto";
        textarea.style.height = (textarea.scrollHeight) + "px";
    }

    
});

