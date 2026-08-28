/**
 * NampaWaterHeater.com — Main JavaScript
 * Handles: mobile nav toggle, FAQ accordion, active nav state
 */

(function () {
  'use strict';

  // Mobile navigation toggle
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileNav = document.getElementById('mobile-nav');

  if (mobileMenuBtn && mobileNav) {
    mobileMenuBtn.addEventListener('click', function () {
      const isOpen = mobileNav.classList.toggle('open');
      mobileMenuBtn.setAttribute('aria-expanded', isOpen.toString());
      // Toggle icon
      const icon = mobileMenuBtn.querySelector('.menu-icon');
      if (icon) {
        icon.innerHTML = isOpen
          ? '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>'
          : '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>';
      }
    });
  }

  // FAQ Accordion
  const faqQuestions = document.querySelectorAll('.faq-question');

  faqQuestions.forEach(function (btn) {
    btn.addEventListener('click', function () {
      const answer = this.nextElementSibling;
      const isOpen = answer.classList.contains('open');

      // Close all open answers
      document.querySelectorAll('.faq-answer.open').forEach(function (a) {
        a.classList.remove('open');
        a.previousElementSibling.classList.remove('open');
      });

      // Open clicked if it was closed
      if (!isOpen) {
        answer.classList.add('open');
        this.classList.add('open');
      }
    });
  });

  // Mark active nav link based on current page
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.main-nav a, .mobile-nav a');

  navLinks.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href && currentPath.endsWith(href.replace('../', '').replace('./', ''))) {
      link.classList.add('active');
    }
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();
