<?php

$receiving_email_address = 'abdulquddus51@gmail.com';

if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'POST') {
  $from_name = $_POST['name'] ?? '';
  $from_email = $_POST['email'] ?? '';
  $subject = $_POST['subject'] ?? '';
  $message = $_POST['message'] ?? '';

  // Send email using a suitable method or library
  // For example, you can use the built-in mail() function:
  $headers = "From: $from_name <$from_email>\r\n";
  $headers .= "Reply-To: $from_email\r\n";
  $headers .= "Content-type: text/plain; charset=utf-8\r\n";

  if (mail($receiving_email_address, $subject, $message, $headers)) {
    echo "Email sent successfully";
  } else {
    echo "Failed to send email";
  }
} else {
  echo "Invalid request";
}
?>
