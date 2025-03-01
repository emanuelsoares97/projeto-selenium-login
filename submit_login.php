<?php
// Simulação de dados de usuário e senha válidos
$usuarioCorreto = "usuario";
$senhaCorreta = "senha123";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = $_POST['username'];
    $senha = $_POST['password'];

    if ($usuario === $usuarioCorreto && $senha === $senhaCorreta) {
        // Redirecionar para a página de registro
        header("Location: pagregisto.html"); // Ajuste o nome do arquivo conforme necessário
        exit();
    } else {
        echo "Usuário ou senha incorretos!";
    }
} else {
    echo "Método inválido.";
}
?>
