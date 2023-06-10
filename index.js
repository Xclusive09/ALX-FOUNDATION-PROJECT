document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission
  
    // Fetch form data
    const formData = new FormData(this);
  
    // Send AJAX request to server-side component
    fetch('/home/xclusive/Desktop/ALX-FOUNDATION PROJECT/forms/contact.php', {
      method: 'POST',
      body: formData
    })
    .then(response => response.text())
    .then(result => {
      // Display result message to the user
      document.getElementById('resultMessage').textContent = result;
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
  