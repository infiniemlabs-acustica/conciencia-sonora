<?php
$cname = $_POST["name"];
$cemail = $_POST["email"];
$cmessage = $_POST["message"];
 
$EmailTo = "infiniemlab.dsp@gmail.com";
$Subject = "New Message Received";
 
// prepare email body text
$Body .= "Name: ";
$Body .= $cname;
$Body .= "\n";
 
$Body .= "Email: ";
$Body .= $cemail;
$Body .= "\n";
 
$Body .= "Message: ";
$Body .= $cmessage;
$Body .= "\n";
 
// send email
$success = mail($EmailTo, $Subject, $Body, "From:".$cemail);
 
// redirect to success page
if ($success){
   echo "success";
}else{
    echo "invalid";
}
 
?>
