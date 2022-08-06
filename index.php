 <!DOCTYPE html>
<html>
<body>

<?php
$result = shell_exec( 'cd script; python3 verify.py '. escapeshellarg ( $_GET["u"] ). " ". escapeshellarg ($_GET["g"]) );
echo $result, PHP_EOL;
?>

</body>
</html> 