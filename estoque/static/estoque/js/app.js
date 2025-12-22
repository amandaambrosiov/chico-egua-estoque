document.addEventListener("DOMContentLoaded", function () {

    setTimeout(() => {
        document.querySelectorAll('.toast-message, .message').forEach(el => el.remove());
    }, 5000);

    const telefone = document.getElementById("telefone");
    if (telefone) {
        telefone.addEventListener("input", function () {
            let value = telefone.value.replace(/\D/g, "");
            value = value.replace(/^(\d{2})(\d)/g, "($1) $2");
            value = value.replace(/(\d)(\d{4})$/, "$1-$2");
            telefone.value = value;
        });
    }

    const modal = document.getElementById('modalConfirmacao');

    if (modal) {
        modal.addEventListener('show.bs.modal', function (event) {
            const btn = event.relatedTarget;

            document.getElementById('modalTitulo').innerHTML = btn.dataset.titulo || 'Confirmação';
            document.getElementById('modalMensagem').innerHTML = btn.dataset.mensagem || '';

            const confirmar = document.getElementById('modalBotaoConfirmar');
            confirmar.className = 'btn ' + (btn.dataset.btnClass || 'btn-primary');
            confirmar.innerHTML = btn.dataset.btn || 'Confirmar';

            confirmar.onclick = function () {
                if (btn.dataset.submit) {
                    document.getElementById(btn.dataset.submit).submit();
                } else if (btn.dataset.url) {
                    window.location.href = btn.dataset.url;
                }
            };
        });
    }

    const searchInput = document.querySelector('input[name="q"]');

    if (searchInput) {
        let timeout;

        searchInput.addEventListener('input', () => {
            clearTimeout(timeout);

            if (searchInput.value.length < 3) return;

            timeout = setTimeout(() => {
                searchInput.form.submit();
            }, 400);
        });
    }

});
