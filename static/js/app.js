function confirmarExclusao() {
    return window.confirm("Tem certeza de que deseja excluir este livro?");
}

// Registra o Service Worker do PWA quando o navegador oferece suporte.
if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
        navigator.serviceWorker.register("/static/sw.js").catch((erro) => {
            console.error("Falha ao registrar o Service Worker:", erro);
        });
    });
}
