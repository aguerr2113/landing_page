// // Select the cta-button element using its ID
// const ctaButton = document.getElementById('cta-button');
// // Add a click event listener to the cta-button element
// ctaButton.addEventListener('click', function() {
//   // Redirect the user to the signup.html file
//   window.location.href = 'signup.html';
// });


// Select the body and the signup form using their IDs
// Select the body and the signup form using their IDs
const body = document.getElementById('body');
const signupForm = document.getElementById('signup-form');

// Add event listeners to the signup form
signupForm.addEventListener('mouseenter', function() {
  // When the mouse enters the form, set the body opacity to 1 (fully visible)
  body.style.opacity = '1';
});
signupForm.addEventListener('mouseleave', function() {
  // When the mouse leaves the form, set the body opacity back to 0.9
  body.style.opacity = '0.6';
});
signupForm.addEventListener('focusin', function() {
  // When a form element is focused, set the body opacity to 1 (fully visible)
  body.style.opacity = '1';
});
signupForm.addEventListener('focusout', function() {
  // When a form element loses focus, set the body opacity back to 0.9
  body.style.opacity = '0.6';
});
