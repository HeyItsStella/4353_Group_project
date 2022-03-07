<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8"> 
    <link rel="stylesheet" href="../cssFiles/registrationCss.css">
    <title>Registration</title>
  </head>
  <body>
    <a class="home" href="../index.html">Home</a>
    <div class="container">

    <form method="POST">
    <h1> "Create an Account" </h1>
    <p class="line1"> Username  <br>  <input placeholder="Enter email or username" name="user"/> </p>
    <p class="line2"> Password   <br>  <input placeholder="Enter password" name="pass"/> </p>
    <p class="line3">  Confirm Password  <br> <input placeholder="Re—enter your Password" name="pass"/>  </p>
    
    <ul class="line4"> 
    <li>Must be between 8-64 characters</li>
    <li>Must include a capital letter and a number</li>
    </ul>
    <p class="line3"> <input type="submit" name="submit"> </p>
    <!--<p class= "button"> <a href="../pages/registration.html" > Register</a> </p>-->
    <!--https://developer.mozilla.org/zh-CN/docs/Learn/CSS/Styling_text/Web_fonts-->
    </form>

    </div>

</body>
</html>

<?php
              
if(isset($_POST['user']))
{
$data=$_POST['user'] . " ";
$fp = fopen('data.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}
if(isset($_POST['pass']))
{
$data=$_POST['pass'] . " ";
$fp = fopen('data.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}

?>