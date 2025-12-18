setTimeout(() => {
            document.querySelectorAll('.toast-message').forEach(el => el.remove());
        }, 5000);

document.addEventListener("DOMContentLoaded", function () {
    const telefone = document.getElementById("telefone");

    if (telefone) {
        telefone.addEventListener("input", function () {
            let value = telefone.value.replace(/\D/g, "");
            value = value.replace(/^(\d{2})(\d)/g, "($1) $2");
            value = value.replace(/(\d)(\d{4})$/, "$1-$2");
            telefone.value = value;
        });
    }
});

