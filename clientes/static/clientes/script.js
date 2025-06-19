// Espera que todo el contenido del DOM esté cargado antes de ejecutar el script
document.addEventListener("DOMContentLoaded", function () {
    // Obtiene el formulario por su ID
    const form = document.getElementById("formularioCliente");

    // Obtiene el párrafo donde se mostrarán los mensajes de validación
    const mensaje = document.getElementById("mensajeValidacion");

    // Escucha el evento "submit" del formulario
    form.addEventListener("submit", function (e) {
        // Obtiene y limpia los valores de los campos
        const nombre = document.getElementById("nombre").value.trim();
        const email = document.getElementById("email").value.trim();

        // Verifica si algún campo está vacío
        if (nombre === "" || email === "") {
            e.preventDefault(); // Detiene el envío del formulario
            mensaje.textContent = "Todos los campos son obligatorios."; // Muestra mensaje
        } else {
            mensaje.textContent = ""; // Borra el mensaje si todo está bien
        }
    });
});
