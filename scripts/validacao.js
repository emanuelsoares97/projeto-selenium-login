
// validar se o url tem erro
window.onload = function () {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('erro') === '1') {
        alert("Utilizador ou password incorretos!");
    }
};


