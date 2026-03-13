<?php
//variáveis para conexão à BD
$host = "localhost";
$user = "root";
$pass = "";
$dbname = "hospital_db";
$port = 3306;

try {
    $conn = new PDO("mysql:host=$host;dbname=$dbname;port=$port;charset=utf8", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $err) {
    die("Erro: Conexão com BD falhou. Erro gerado: " . $err->getMessage());
}
?>