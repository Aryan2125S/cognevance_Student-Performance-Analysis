document.addEventListener('DOMContentLoaded', () => {
    // 1. Theme Toggle Logic (Light / Dark Mode)
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;
    const themeIcon = themeToggleBtn.querySelector('i');
    
    // Check local storage or system preference
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    const applyTheme = (theme) => {
        if (theme === 'dark') {
            htmlElement.setAttribute('data-theme', 'dark');
            themeIcon.className = 'fa-solid fa-sun';
            themeToggleBtn.style.color = '#e2e8f0';
        } else {
            htmlElement.removeAttribute('data-theme');
            themeIcon.className = 'fa-solid fa-moon';
            themeToggleBtn.style.color = '#1e293b';
        }
    };
    
    // Initial application
    if (savedTheme) {
        applyTheme(savedTheme);
    } else if (systemPrefersDark) {
        applyTheme('dark');
    }
    
    // Toggle click event
    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = htmlElement.getAttribute('data-theme');
        if (currentTheme === 'dark') {
            localStorage.setItem('theme', 'light');
            applyTheme('light');
        } else {
            localStorage.setItem('theme', 'dark');
            applyTheme('dark');
        }
    });

    // 2. Set Current Date Dynamically
    const dateBadge = document.getElementById('current-date');
    if (dateBadge) {
        const options = { month: 'long', year: 'numeric' };
        const currentDate = new Date().toLocaleDateString('en-US', options);
        dateBadge.textContent = currentDate;
    }

    // 3. Highlight Sidebar Active Nav (Fail-safe)
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('.nav-item');
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href && currentPath === href) {
            navItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
        }
    });
    
    console.log("EduMetrics Dashboard script loaded successfully.");
});
