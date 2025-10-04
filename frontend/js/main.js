// Webmaster Frontend JavaScript
// Main JavaScript functionality for the website

// Projects Carousel functionality
class ProjectsCarousel {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.isDown = false;
        this.startX = 0;
        this.scrollLeft = 0;
        
        if (this.container) {
            this.init();
        }
    }
    
    init() {
        this.container.addEventListener('mousedown', (e) => {
            this.isDown = true;
            this.container.classList.add('active');
            this.startX = e.pageX - this.container.offsetLeft;
            this.scrollLeft = this.container.scrollLeft;
        });

        this.container.addEventListener('mouseleave', () => {
            this.isDown = false;
            this.container.classList.remove('active');
        });

        this.container.addEventListener('mouseup', () => {
            this.isDown = false;
            this.container.classList.remove('active');
        });

        this.container.addEventListener('mousemove', (e) => {
            if (!this.isDown) return;
            e.preventDefault();
            const x = e.pageX - this.container.offsetLeft;
            const walk = (x - this.startX) * 2;
            this.container.scrollLeft = this.scrollLeft - walk;
        });
    }
}

// Form submission functionality
class FormHandler {
    constructor(formId, apiEndpoint) {
        this.form = document.getElementById(formId);
        this.apiEndpoint = apiEndpoint;
        
        if (this.form) {
            this.init();
        }
    }
    
    init() {
        this.form.addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleSubmit();
        });
    }
    
    async handleSubmit() {
        const formData = new FormData(this.form);
        const data = Object.fromEntries(formData.entries());
        
        // Show loading state
        const submitBtn = this.form.querySelector('.submit-btn');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Submitting...';
        submitBtn.disabled = true;
        
        try {
            const response = await fetch(this.apiEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    ...data,
                    form_type: 'price_calculator'
                })
            });
            
            const result = await response.json();
            
            if (result.success) {
                this.showSuccess(data.name, data.phone, data.email);
                this.form.reset();
            } else {
                this.showError(result.error || 'Unknown error occurred');
            }
        } catch (error) {
            console.error('Form submission error:', error);
            this.showError('Network error. Please try again.');
        } finally {
            // Reset button state
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }
    }
    
    showSuccess(name, phone, email) {
        alert(`Thank you, ${name}! Your request has been submitted. We will contact you at ${phone} or ${email} shortly.`);
    }
    
    showError(message) {
        alert(`Error: ${message}`);
    }
}

// Dropdown menu functionality
class DropdownMenu {
    constructor() {
        this.dropdowns = document.querySelectorAll('.dropdown');
        this.init();
    }
    
    init() {
        this.dropdowns.forEach(dropdown => {
            const trigger = dropdown.querySelector('a');
            const menu = dropdown.querySelector('.dropdown-menu');
            
            if (trigger && menu) {
                dropdown.addEventListener('mouseenter', () => {
                    menu.style.opacity = '1';
                    menu.style.visibility = 'visible';
                    menu.style.transform = 'translateY(0)';
                });
                
                dropdown.addEventListener('mouseleave', () => {
                    menu.style.opacity = '0';
                    menu.style.visibility = 'hidden';
                    menu.style.transform = 'translateY(-10px)';
                });
            }
        });
    }
}

// Smooth scrolling for navigation links
class SmoothScroll {
    constructor() {
        this.navLinks = document.querySelectorAll('a[href^="#"]');
        this.init();
    }
    
    init() {
        this.navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                const targetId = link.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    e.preventDefault();
                    targetElement.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }
}

// Initialize all components when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Initialize projects carousel
    new ProjectsCarousel('projectsContainer');
    
    // Initialize form handler
    new FormHandler('priceCalculator', '/api/submit-form');
    
    // Initialize dropdown menus
    new DropdownMenu();
    
    // Initialize smooth scrolling
    new SmoothScroll();
    
    // Add loading animation
    const loadingElements = document.querySelectorAll('.loading');
    loadingElements.forEach(element => {
        element.classList.add('animate-pulse');
    });
});

// Utility functions
const Utils = {
    // Format phone number
    formatPhoneNumber(phone) {
        const cleaned = phone.replace(/\D/g, '');
        const match = cleaned.match(/^(\d{3})(\d{3})(\d{4})$/);
        if (match) {
            return '(' + match[1] + ') ' + match[2] + '-' + match[3];
        }
        return phone;
    },
    
    // Validate email
    validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    },
    
    // Show notification
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500' : 
            type === 'error' ? 'bg-red-500' : 
            'bg-blue-500'
        } text-white`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
};

// Export for use in other scripts
window.Webmaster = {
    ProjectsCarousel,
    FormHandler,
    DropdownMenu,
    SmoothScroll,
    Utils
};
