
<?php

	set_time_limit(200);

	echo("hello, be");

	$URL = 'http://i.imgur.com/1VFEpu9.jpg';

	$term = "/usr/bin/python3 /home/legion/Documents/project/uclassify.py ".$URL." 2>&1";

	$command = escapeshellcmd($term);

	$output = shell_exec($term);

	echo "<pre> $output </pre>";

	//$_POST = ['params'];



?>
