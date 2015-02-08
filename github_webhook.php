<?php

shell_exec("cd ~/website");
$output = shell_exec("git pull");
shell_exec("touch dispatch.fcgi");
shell_exec("touch tmp/restart.txt");
echo $output;
