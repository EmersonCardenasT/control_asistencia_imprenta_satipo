
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
                    let timerInterval;
                    Swal.fire({
                        title: "BIENVENIDO",
                        html: "Se redireccionara en <b></b> milisegundos.",
                        timer: 1500,
                        timerProgressBar: true,
                        didOpen: () => {
                            Swal.showLoading();
                            const timer = Swal.getPopup().querySelector("b");
                            timerInterval = setInterval(() => {
                                timer.textContent = `${Swal.getTimerLeft()}`;
                            }, 100);
                        },
                        willClose: () => {
                            clearInterval(timerInterval);
                        }
                    }).then((result) => {
                        /* Read more about handling dismissals below */
                        if (result.dismiss === Swal.DismissReason.timer) {
                            window.location = BASE_URL + "Administracion/home";
                        }
                    });
                } else {
                    document.getElementById("alerta").classList.remove("d-none");
                    document.getElementById("alerta").innerHTML = res;
                }
            }
        }

    }

}


