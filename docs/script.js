///// Funciones para cambiar graficos

// Graficos Pregunta 5
document.addEventListener("DOMContentLoaded", () => {
    const selector = document.getElementById("selector-grafico-p5");
    const imagen = document.getElementById("grafico-p5");

    selector.addEventListener("change", function () {
        imagen.src = this.value;
    });
});

// Graficos Pregunta 3
document.addEventListener("DOMContentLoaded", () => {
    const selector = document.getElementById("selector-grafico-p3");
    const imagen = document.getElementById("grafico-p3");

    selector.addEventListener("change", function () {
        imagen.src = this.value;
    });
});

//   <!-- ========== SCRIPT: desplegar/ocultar preguntas ========== -->
document.addEventListener('DOMContentLoaded', function () {
        const linkAnalisis = document.getElementById('link-analisis');
        const subpreguntas = document.querySelector('.subpreguntas');

        linkAnalisis.addEventListener('click', function (e) {
            e.preventDefault();
            subpreguntas.classList.toggle('activa');

            const analisis = document.getElementById('analisis');
            if (analisis) {
                analisis.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });