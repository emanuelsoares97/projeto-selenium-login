<?php
// Simulação de usuário e senha corretos
$usuarioCorreto = "user1";
$senhaCorreta = "pass1";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = $_POST['username'];
    $senha = $_POST['password'];

    if ($usuario === $usuarioCorreto && $senha === $senhaCorreta) {
        // Login bem-sucedido → Redireciona para a página de registro
        header("Location: pagregisto.html");
        exit();
    } else {
        // Login falhou → Redireciona para o login com erro
        header("Location: index.html?erro=1");
        exit();
    }
} else {
    echo "Método inválido.";
}
?>
