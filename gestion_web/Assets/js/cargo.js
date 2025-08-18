// CARGOS
function frmCargo() {
    document.getElementById("title").innerHTML = "Nuevo cargo";
    document.getElementById("btnAccion").innerHTML = "Registrar";
    document.getElementById("frmCargo").reset();
    $("#nuevo_cargo").modal("show");
    document.getElementById("id").value = "";
}

function registrarCargo(e) {
    e.preventDefault();
    const cargo = document.getElementById("cargo");

    if (cargo.value == "") {
        Swal.fire({
            title: "Info",
            text: "Por favor completar el campo cargo!",
            icon: "warning"
          });
        document.getElementById("cargo").focus();

    } else {
        const url = BASE_URL + "Cargo/registrar";
        const frm = document.getElementById("frmCargo");
        const http = new XMLHttpRequest();
        http.open("POST", url, true);
        http.send(new FormData(frm));
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                const res = JSON.parse(this.responseText);
                frm.reset();
                $("#nuevo_cargo").modal("hide");
                alertas(res.msg, res.icono, res.titulo);
                tblCargo.ajax.reload();
            }
        }
    }

}

function btnEditarCargo(id) {
    document.getElementById("title").innerHTML = "Actualizar cargo";
    document.getElementById("btnAccion").innerHTML = "Modificar";

    const url = BASE_URL + "Cargo/editar/" + id;
    const http = new XMLHttpRequest();
    http.open("GET", url, true);
    http.send();
    http.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            const res = JSON.parse(this.responseText);
            document.getElementById("id").value = res.id;
            document.getElementById("cargo").value = res.nombre;
            $("#nuevo_cargo").modal("show");
        }
    }

}

function btnEliminarCargo(id) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: "btn btn-primary",
            cancelButton: "btn btn-danger"
        },
        // buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
        title: "Estas seguro de eliminar el cargo?",
        text: "El cargo sera eliminado permanentemente!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, eliminar!",
        cancelButtonText: "No, cancelar!",
        reverseButtons: false
    }).then((result) => {
        if (result.isConfirmed) {
            const url = BASE_URL + "Cargo/eliminar/" + id;
            const http = new XMLHttpRequest();
            http.open("GET", url, true);
            http.send();
            http.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    const res = JSON.parse(this.responseText);
                    alertas(res.msg, res.icono, res.titulo);
                    tblCargo.ajax.reload();
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
// FIN CARGOS