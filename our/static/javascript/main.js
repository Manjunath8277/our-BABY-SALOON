const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});




// function submitForm(event) {
//   event.preventDefault(); // Prevent default form submission
  
//   // Get form data
//   const formData = new FormData(document.getElementById('loginform'));
//   const fullName = formData.get('text');
//   const password = formData.get('password');
//   const email = formData.get('email');
//   alert ( "succesfulley signuped");   
//   // You can perform validation here if needed
  
//   // Redirect to website page
//   window.location.href = 'http://127.0.0.1:5500/our/templates/secondpg.html'; // Change the URL to your desired destination
// }