// Sticky Header & Scroll Direction
let lastScroll = 0;
const nav = document.querySelector('nav');

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    // Background Blur/Opacity on scroll
    if (currentScroll > 50) {
        nav.classList.add('bg-forest/95', 'shadow-2xl');
        nav.classList.remove('bg-forest/80');
    } else {
        nav.classList.remove('bg-forest/95', 'shadow-2xl');
        nav.classList.add('bg-forest/80');
    }

    // Hide/Show on scroll direction
    if (currentScroll > lastScroll && currentScroll > 150) {
        // Scrolling down
        nav.style.transform = 'translateY(-100%)';
    } else {
        // Scrolling up
        nav.style.transform = 'translateY(0)';
    }
    
    lastScroll = currentScroll;

    // Parallax effect for Hero Video
    const video = document.querySelector('video');
    if (video) {
        video.style.transform = `translateY(${currentScroll * 0.4}px)`;
    }
});

// Scroll Reveal Animation
const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        } else if (entry.boundingClientRect.top > 0) {
            // Optional: Remove active class when scrolling back up past the element
            // entry.target.classList.remove('active');
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => observer.observe(el));
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
