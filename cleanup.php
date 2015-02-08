<?php

// Set permissions
$perms = array(
    "700 github_webhook.php",
);
foreach ($perms as $perm)
{
    echo shell_exec("chmod " . $perm);
}
