let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".sidebarBtn");
sidebarBtn.onclick = function () {
  sidebar.classList.toggle("active");
  if (sidebar.classList.contains("active")) {
    sidebarBtn.classList.replace("bx-menu", "bx-menu-alt-right");
  } else sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
};



const toggleDropdown = document.getElementById('toggle-dropdown');
    const dropdownMenu = document.getElementById('dropdown-menu');

    toggleDropdown.addEventListener('click', () => {
        dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
    });

    // Cierra el dropdown si se hace clic fuera
    window.addEventListener('click', (event) => {
        if (!dropdownMenu.contains(event.target) && event.target !== toggleDropdown) {
            dropdownMenu.style.display = 'none';
        }
    });