<?php
$directory = '/images'; // Directory path to your images

if (is_dir($directory)) {
    $files = scandir($directory);
    foreach ($files as $file) {
        if (is_file($directory . '/' . $file)) {
            echo '<li class="glide__slide"><img src="' . $directory . '/' . $file . '" alt=""></li>';
        }
    }
}
?>
