/**
 * Bistro Loft - Clone Script
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mobileNavMenu = document.getElementById('mobile-nav-menu');

    if (mobileMenuToggle && mobileNavMenu) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileMenuToggle.classList.toggle('is-active');
            mobileNavMenu.classList.toggle('is-open');
        });
    }

    // 2. Sticky Header Implementation
    const header = document.getElementById('main-header');
    if (header) {
        let lastScrollY = window.scrollY;

        const handleScroll = () => {
            const currentScrollY = window.scrollY;

            // Add sticky class when scrolling down a bit
            if (currentScrollY > 100) {
                header.classList.add('is-sticky');
            } else {
                header.classList.remove('is-sticky');
            }

            lastScrollY = currentScrollY;
        };

        window.addEventListener('scroll', handleScroll, { passive: true });
    }
});
