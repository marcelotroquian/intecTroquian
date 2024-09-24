document.addEventListener('DOMContentLoaded', function () {
  var errorMessage = document.getElementById('error-message');

  if (errorMessage) {
      function showError() {
          errorMessage.style.display = 'block';  // Asegurarse de que el contenedor está visible
          errorMessage.classList.add('show');   // Añadir la clase que activa la transición

          // Configurar un temporizador para ocultar el mensaje después de 5 segundos (5000 milisegundos)
          setTimeout(function () {
              errorMessage.classList.remove('show'); // Eliminar la clase para ocultar con transición
              // Esperar la duración de la transición antes de ocultar el elemento completamente
              setTimeout(function () {
                  errorMessage.style.display = 'none';
              }, 500); // 500 ms corresponde a la duración de la transición CSS
          }, 5000); // 5000 ms corresponde al tiempo que el mensaje de error permanece visible
      }

      if (errorMessage.innerHTML.trim()) {
          showError();
      }
  }
});




document.getElementById('keepSessionCheckbox').addEventListener('change', function() {
    // Verificar si el checkbox está marcado
    if (this.checked) {
      // Si está marcado, establecer un indicador de sesión activa en localStorage
      localStorage.setItem('sessionActive', 'true');
      
    } else {
      // Si no está marcado, eliminar el indicador de sesión activa de localStorage
      localStorage.removeItem('sessionActive');
    }
  });
