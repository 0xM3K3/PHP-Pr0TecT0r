#!/usr/bin/python
# Michael.Maher
# www.github.com/Micro-EG
import os

os.system('cls' if os.name == 'nt' else 'clear')
 
print ('''
+------------------------------------+
   ___       __  __ _____ _  _______ 
  / _ \__  _|  \/  |___ /| |/ /___ /
 | | | \ \/ / |\/| | |_ \| ' /  |_ \ 
 | |_| |>  <| |  | |___) | . \ ___) |
  \___//_/\_\_|  |_|____/|_|\_\____/ 
 									   

         PHP-Pr0TecT0r v0.1
+------------------------------------+
''')
 
#########################################
p=input("\nPassword : ")
pat=input("\nPath : ")
#########################################
line = '''<?php

###########################
# Michael.Maher           #
# www.github.com/Micro-EG #
###########################

@$pass = $_POST['pass'];
$chk_login = true;
$password = "'''+p+'''";


if($pass == $password)
{
 $nst = "$pass";
}

if($chk_login == true)
{
 if(!isset($nst) or $nst != $password)
 {
 die("
  <html>
  <head>
  <title> Pr0tect PAG3 </title></head>
  <body bgcolor=black >
  <center>
  <table border=0 cellpadding=0 cellspacing=0 width=100% height=100%>
  <tr><td valign=middle align=center>
  <table width=100 bgcolor=white border=6 bordercolor=blue><tr><td>
  <font size=1 face=verdana><center>
  <b></font></a><br></b>
  </center>
  <form method=post>
  <font size=1 face=verdana color=black><strong><center>-ENT3R Th3 PASS-
  </center></strong><br>
  <input type=password name=pass size=30>
  </form>
  <b>Your ip : </b> ".$_SERVER["REMOTE_ADDR"]."
  </td></tr></table>
  </td></tr></table>
  </body>
  </html>
  ");
 }
}
 ?>'''
with open(pat, 'r+') as f:
    file_data = f.read()
    f.seek(0, 0)
    f.write(line.rstrip('\r\n') + '\n' + file_data)
