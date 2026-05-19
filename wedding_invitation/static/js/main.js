document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('nav');
    const menuToggle = document.querySelector('[data-menu-toggle]');
    const mobileMenu = document.getElementById('mobile-menu');
    const toast = document.getElementById('site-toast');

    if (!navbar) {
        return;
    }

    const updateNavbar = () => {
        navbar.classList.toggle('shadow-2xl', window.scrollY > 20);
    };

    updateNavbar();
    window.addEventListener('scroll', updateNavbar, { passive: true });

    document.querySelectorAll('.nav-link').forEach((link) => {
        const linkPath = new URL(link.href).pathname;
        const currentPath = window.location.pathname;

        if (linkPath === currentPath || (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
        }
    });

    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', () => {
            const isOpen = mobileMenu.classList.toggle('open');
            menuToggle.setAttribute('aria-expanded', String(isOpen));
            menuToggle.setAttribute('aria-label', isOpen ? 'Fermer le menu' : 'Ouvrir le menu');
        });
    }

    const params = new URLSearchParams(window.location.search);
    const hasSubmittedRsvp = params.has('attendance') && params.has('name');
    const hasSubmittedGuestbook = params.has('message') && window.location.pathname.includes('guestbook');

    if (toast && (hasSubmittedRsvp || hasSubmittedGuestbook)) {
        toast.textContent = hasSubmittedRsvp
            ? 'Merci, votre reponse a bien ete prise en compte pour la preparation.'
            : 'Merci pour votre message. Il sera precieux pour les maries.';
        toast.classList.add('show');

        setTimeout(() => {
            toast.classList.remove('show');
        }, 5200);
    }
});
