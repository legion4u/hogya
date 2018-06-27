

 <?php


$bb=file_get_contents('php://input');
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = $bb;
fwrite($myfile, $txt);

echo $myfile;

fclose($myfile);


?> 