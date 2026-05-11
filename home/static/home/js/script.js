//DOM Elements
const track = document.getElementById("carouselTrack");
const cards = document.querySelectorAll(".carousel-card");

let currentIndex = 0;

const totalCards = cards.length;

function nextSlide() {
    currentIndex = (currentIndex + 1) % totalCards;

    track.style.transform = 
        `translateX(-${currentIndex * 100}%)`;
}

setInterval(nextSlide, 4000);