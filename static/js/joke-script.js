const texts = [
    "Joke's on You (Literally)",
    "Warning: Hilarity Zone",
    "Tickle Your Funny Bone!",
    "Punny Business Only!",
    'Dad Jokes & Beyond',
    'Where Bad Jokes Go to Shine😉',
    'Crack Up Here - No Refunds!'
];

let currentIndex = 0;
let charIndex = 0;
let isDeleting = false;
const typeSpeed = 100; // Speed of typing
const deleteSpeed = 50; // Speed of deleting
const delayBetweenTexts = 1500; // Delay before starting to delete text

function typewriterEffect() {
    const element = document.getElementById("typewriter");
    const currentText = texts[currentIndex];

    if (isDeleting) {
        element.textContent = currentText.substring(0, charIndex--);
        if (charIndex < 0) {
            isDeleting = false;
            currentIndex = (currentIndex + 1) % texts.length;
            setTimeout(typewriterEffect, typeSpeed);
        } else {
            setTimeout(typewriterEffect, deleteSpeed);
        }
    } else {
        element.textContent = currentText.substring(0, charIndex++);
        if (charIndex > currentText.length) {
            isDeleting = true;
            setTimeout(typewriterEffect, delayBetweenTexts);
        } else {
            setTimeout(typewriterEffect, typeSpeed);
        }
    }
}

// Start the typewriter effect
document.addEventListener("DOMContentLoaded", function() {
    typewriterEffect();
});
