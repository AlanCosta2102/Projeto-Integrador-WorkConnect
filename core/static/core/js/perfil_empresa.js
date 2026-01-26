document.addEventListener("DOMContentLoaded", function () {
  const btnEditar = document.getElementById("btn-editar");
  const formEdicao = document.getElementById("form-edicao");

  if (btnEditar && formEdicao) {
    btnEditar.addEventListener("click", function () {
      formEdicao.style.display = "block";
      btnEditar.style.display = "none";
    });
  }
});
document.getElementById('btn-editar').addEventListener('click', function () {
        const form = document.getElementById('form-edicao-wrapper');
        form.style.display = form.style.display === 'none' ? 'block' : 'none';
    });
