<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    echo "POST is working";
} else {
    echo "Wrong method: " . $_SERVER["REQUEST_METHOD"];
}
?>
