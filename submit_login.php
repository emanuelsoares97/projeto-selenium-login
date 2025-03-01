<?php
// Simulação de dados de utilizador e pass
$utilizadorCorreto = "user1";
$senhaCorreta = "pass1";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $utilizador = $_POST['username'];
    $senha = $_POST['password'];

    if ($utilizador === $utilizadorCorreto && $senha === $senhaCorreta) {
        // Redirecionar para a página de registro
        header("Location: pagregisto.html"); // Certifique-se de que o nome do arquivo está correto
        exit();
    } else {
        echo "Usuário ou senha incorretos!";
    }
} else {
    echo "Método inválido.";
}
?>
