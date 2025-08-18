<?php

spl_autoload_register(function($class){
    $paths = [
        "Config/App/$class.php",
        "Controllers/$class.php",
        "Models/$class.php"
    ];

    foreach ($paths as $path) {
        if (file_exists($path)) {
            require_once $path;
            break;
        }
    }
});

?>
