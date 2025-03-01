// Seleciona os elementos
const btnRegistrar = document.getElementById("btnRegistrar");
const modal = document.getElementById("modal");
const btnCancelar = document.getElementById("btnCancelar");
const btnConfirmar = document.getElementById("btnConfirmar");
const barraSucesso = document.getElementById("barraSucesso");
const horaAtual = document.getElementById("horaAtual");

// Atualiza a hora ao abrir o modal
function atualizarHora() {
    const agora = new Date();
    const horas = agora.getHours().toString().padStart(2, "0");
    const minutos = agora.getMinutes().toString().padStart(2, "0");
    const segundos = agora.getSeconds().toString().padStart(2, "0");
    horaAtual.textContent = `${horas}:${minutos}:${segundos}`;
}

// Evento para abrir o modal
btnRegistrar.addEventListener("click", () => {
    atualizarHora();
    modal.style.display = "flex";
});

// Evento para cancelar (fechar o modal)
btnCancelar.addEventListener("click", () => {
    modal.style.display = "none";
});

// Evento para confirmar (fecha o modal e exibe a barra de sucesso)
btnConfirmar.addEventListener("click", () => {
    modal.style.display = "none";
    barraSucesso.style.display = "block";

    // Remove a barra de sucesso após 3 segundos
    setTimeout(() => {
        barraSucesso.style.display = "none";
    }, 3000);
});
