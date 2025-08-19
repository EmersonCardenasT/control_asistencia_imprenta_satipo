// TURNOS
function frmTurnos() {
    document.getElementById("title").innerHTML = "Nuevo turno";
    document.getElementById("btnAccion").innerHTML = "Registrar";
    document.getElementById("frmTurnos").reset();
    $("#nuevo_turno").modal("show");
    document.getElementById("id").value = "";
}

function registrarTurno(e) {
    e.preventDefault();
    const turno = document.getElementById("turno");
    const hora_entrada = document.getElementById("hora_entrada");
    const hora_salida = document.getElementById("hora_salida");

    if (turno.value == "" || hora_entrada.value == "" || hora_salida.value == "") {
        Swal.fire({
            title: "Info",
            text: "Por favor completar los campos vacios",
            icon: "warning"
          });
        document.getElementById("turno").focus();

    } else {
        const url = BASE_URL + "Horario/registrar";
        const frm = document.getElementById("frmTurnos");
        const http = new XMLHttpRequest();
        http.open("POST", url, true);
        http.send(new FormData(frm));
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                const res = JSON.parse(this.responseText);
                frm.reset();
                $("#nuevo_turno").modal("hide");
                alertas(res.msg, res.icono, res.titulo);
                tblTurnos.ajax.reload();
            }
        }
    }

}

function btnEditarTurno(id) {
    document.getElementById("title").innerHTML = "Actualizar turno";
    document.getElementById("btnAccion").innerHTML = "Modificar";

    const url = BASE_URL + "Horario/editar/" + id;
    const http = new XMLHttpRequest();
    http.open("GET", url, true);
    http.send();
    http.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            const res = JSON.parse(this.responseText);
            document.getElementById("id").value = res.id;
            document.getElementById("turno").value = res.nombre;
            document.getElementById("hora_entrada").value = res.hora_entrada;
            document.getElementById("hora_salida").value = res.hora_salida;
            $("#nuevo_turno").modal("show");
        }
    }

}

function btnEliminarTurno(id) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: "btn btn-primary",
            cancelButton: "btn btn-danger"
        },
        // buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
        title: "Estas seguro de eliminar el turno?",
        text: "El turno sera eliminado permanentemente!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, eliminar!",
        cancelButtonText: "No, cancelar!",
        reverseButtons: false
    }).then((result) => {
        if (result.isConfirmed) {
            const url = BASE_URL + "Horario/eliminar/" + id;
            const http = new XMLHttpRequest();
            http.open("GET", url, true);
            http.send();
            http.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    const res = JSON.parse(this.responseText);
                    alertas(res.msg, res.icono, res.titulo);
                    tblTurnos.ajax.reload();
                }
            }
        } else if (
            /* Read more about handling dismissals below */
            result.dismiss === Swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons.fire({
                title: "Cancelado",
                text: "Tus registros no se modificaron",
                icon: "error"
            });
        }
    });
}
// FIN TURNOS