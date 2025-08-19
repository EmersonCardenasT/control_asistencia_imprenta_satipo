
function frmLogin(e) {
    e.preventDefault();
    const usuario = document.getElementById("usuario");
    const password = document.getElementById("password");

    if (usuario.value == "") {
        password.classList.remove("is-invalid");
        usuario.classList.add("is-invalid");
        usuario.focus();

    } else if (password.value == "") {
        usuario.classList.remove("is-invalid");
        password.classList.add("is-invalid");
        password.focus();

    }else{

        const url = BASE_URL + "Usuario/validar";
        const frm = document.getElementById("frmLogin");
        const http = new XMLHttpRequest();
        http.open("POST", url, true);
        http.send(new FormData(frm));
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                const res = JSON.parse(this.responseText);
                console.log(this.responseText);
                if (res == "ok") {
                        mostrarBarraProgreso();
                } else {
                    document.getElementById("alerta").classList.remove("d-none");
                    document.getElementById("alerta").innerHTML = res;
                }
            }
        }

// Barra de progreso nativa para login exitoso
function mostrarBarraProgreso() {
    // Crear barra si no existe
    let barra = document.getElementById('barra-progreso-login');
    if (!barra) {
        barra = document.createElement('div');
        barra.id = 'barra-progreso-login';
        barra.style.position = 'fixed';
        barra.style.top = '0';
        barra.style.left = '0';
        barra.style.width = '0%';
        barra.style.height = '5px';
        barra.style.background = 'linear-gradient(90deg,#1976d2,#64b5f6)';
        barra.style.zIndex = '9999';
        barra.style.transition = 'width 1.5s linear';
        document.body.appendChild(barra);
    }
    // Animar barra
    setTimeout(() => {
        barra.style.width = '100%';
    }, 50);
    // Redireccionar al terminar
    setTimeout(() => {
        barra.style.display = 'none';
        window.location = BASE_URL + "Administracion/home";
    }, 1600);
}

    }

}


