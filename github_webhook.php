<?php

// Pull and touch
shell_exec("cd ~/website");
$output = shell_exec("git pull");
echo $output;
shell_exec("touch dispatch.fcgi");
shell_exec("touch tmp/restart.txt");

// Rebuild static
shell_exec("rm -r portfolio/static");
shell_exec("source .virtualenv/bin/activate && pip install -r requirements.txt");
shell_exec("source .virtualenv/bin/activate && ./manage.py collectstatic --noinput");
shell_exec("source .virtualenv/bin/activate && ./manage.py syncdb");

// Set permissions
$perms = array(
    "700 cleanup.php",
    "700 dispatch.fcgi",
    "600 portfolio/settings/key.py",
    "600 portfolio/settings/secret.py",
);
foreach ($perms as $perm)
{
    echo shell_exec("chmod " . $perm);
}


echo "Done";
