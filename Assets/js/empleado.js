// FUNCIONES PARA Empleado
function frmEmpleado() {
    document.getElementById("title").innerHTML = "Nuevo Empleado";
    document.getElementById("btnAccion").innerHTML = "Registrar";
    document.getElementById("frmEmpleado").reset();
    $("#modificar_empleado").modal("show");
    document.getElementById("id").value = "";
}

function modificarEmpleado(e) {
    e.preventDefault();
    const nombre = document.getElementById("nombre");
    const apellido = document.getElementById("apellido");
    const dni = document.getElementById("dni");
    const telefono = document.getElementById("telefono");
    const genero = document.getElementById("genero");
    const fecha_nacimiento = document.getElementById("fecha_nacimiento");
    const direccion = document.getElementById("direccion");
    const email = document.getElementById("email");
    const cargos = document.getElementById("cargos");
    const estado = document.getElementById("estado");

    if (nombre.value == "" || apellido.value == "" || telefono.value == "" || genero.value == "" || 
        fecha_nacimiento.value == "" || direccion.value == "" || email.value == "" || cargos.value == "" || estado.value == "") {
        alertas('Todos los campos son obligatorios', 'warning', 'Error');
    } else {
        const url = BASE_URL + "Empleado/modificarEmpleado";
        const frm = document.getElementById("frmEmpleado");
        const http = new XMLHttpRequest();
        http.open("POST", url, true);
        http.send(new FormData(frm));
        http.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                const res = JSON.parse(this.responseText);
                console.log(this.responseText);
                $("#modificar_empleado").modal("hide");
                alertas(res.msg, res.icono, res.titulo);
                tblEmpleado.ajax.reload();
            }
        }
    }
}

function btnEditarEmpleado(id) {
    document.getElementById("title").innerHTML = "Actualizar Empleado";
    document.getElementById("btnAccion").innerHTML = "Modificar";

    const url = BASE_URL + "Empleado/editar/" + id;
    const http = new XMLHttpRequest();
    http.open("GET", url, true);
    http.send();
    http.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.responseText);
            const res = JSON.parse(this.responseText);
            document.getElementById("id").value = res.id;
            document.getElementById("nombre").value = res.nombre;
            document.getElementById("apellido").value = res.apellido;
            document.getElementById("dni").value = res.dni;
            document.getElementById("telefono").value = res.telefono;
            document.getElementById("genero").value = res.genero;
            document.getElementById("fecha_nacimiento").value = res.fecha_nacimiento;
            document.getElementById("direccion").value = res.direccion;
            document.getElementById("email").value = res.email;
            document.getElementById("cargos").value = res.cargo_id;
            document.getElementById("estado").value = res.estado;
            $("#modificar_empleado").modal("show");
        }
    }

}

function btnEliminarEmpleado(id) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: "btn btn-primary",
            cancelButton: "btn btn-danger"
        },
        // buttonsStyling: false
    });
    swalWithBootstrapButtons.fire({
        title: "Estas seguro de eliminar al empleado?",
        text: "El empleado se eliminar de forma permanente!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Si, eliminar!",
        cancelButtonText: "No, cancelar!",
        reverseButtons: false
    }).then((result) => {
        if (result.isConfirmed) {

            const url = BASE_URL + "Empleado/eliminar/" + id;
            const http = new XMLHttpRequest();
            http.open("GET", url, true);
            http.send();
            http.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    const res = JSON.parse(this.responseText);
                    alertas(res.msg, res.icono, res.titulo);
                    tblEmpleado.ajax.reload();
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
