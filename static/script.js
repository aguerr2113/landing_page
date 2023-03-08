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
const form = document.querySelector('#workout-form');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const fitnessLevel = document.querySelector('#fitness-level').value;
  const workoutLength = document.querySelector('#workout-length').value;
  
  fetch('/generate-workout', {
    method: 'POST',
    body: new URLSearchParams({
      'fitness-level': fitnessLevel,
      'workout-length': workoutLength,
    }),
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.workout);
    console.log(data.workout_type);
  })
  .catch(error => console.error(error));
});