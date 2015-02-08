<?php

shell_exec("cd ~/website");
$output = shell_exec("git pull");
echo $output;
shell_exec("touch dispatch.fcgi");
shell_exec("touch tmp/restart.txt");

// Set permissions
$perms = array(
    "700 github_webhook.php",
    "700 dispatch.fcgi",
    "600 portfolio/settings/key.py",
    "600 portfolio/settings/secret.py",
);
foreach ($perms as $perm)
{
    echo shell_exec("chmod " . $perm);
}

shell_exec("rm -r portfolio/static");
shell_exec("source .virtualenv/bin/activate");
shell_exec("./manage.py collectstatic --noinput");
