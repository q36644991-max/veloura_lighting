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
        nav.style.transform = 'translateY(-100%)';
    } else {
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
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', () => {
    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => observer.observe(el));
    
    // Mobile Menu Logic
    const menuToggle = document.querySelector('.menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    const menuLinks = document.querySelectorAll('.mobile-menu a');

    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : 'auto';
        });

        menuLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = 'auto';
            });
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const target = document.querySelector(targetId);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // --- CMS CONTENT LOADER ---
    async function loadSiteContent() {
        try {
            const res = await fetch('/api/content');
            if (!res.ok) return;
            const c = await res.json();
            
            // GLOBAL (Footer/Contact)
            const mapGlobal = {
                'contact-address': c.global.contact_address,
                'contact-email': c.global.contact_email,
                'contact-phone': c.global.contact_phone
            };
            Object.keys(mapGlobal).forEach(id => {
                const el = document.getElementById(id);
                if (el) el.innerText = mapGlobal[id];
            });

            // PAGE SPECIFIC
            const path = window.location.pathname;
            const page = path.includes('about') ? 'about' :
                         path.includes('collections') ? 'collections' :
                         path.includes('portfolio') ? 'portfolio' :
                         path.includes('contact') ? 'contact' :
                         path.includes('booking') ? 'booking' : 'index';
            
            const pageContent = c[page];
            if (pageContent) {
                Object.keys(pageContent).forEach(key => {
                    const id = key.replace(/_/g, '-'); // e.g., hero_title -> hero-title
                    const el = document.getElementById(id);
                    if (el) el.innerText = pageContent[key];
                });
            }
            
        } catch (err) {
            console.log('Using static content (CMS Offline)');
        }
    }

    loadSiteContent();
});
