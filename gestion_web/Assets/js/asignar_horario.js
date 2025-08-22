// BUSCAR CODIGO VENTA
function buscarEmpleado(e) {
    e.preventDefault(); //Esto es para que la pagina no se recargue
    const dni = document.getElementById("dni").value;
    if (dni != '') {
        if (e.which == 13) { //Si el usuario presiona la tecla enter
            const url = BASE_URL + "Empleado/buscarEmpleado/" + dni; //El controlador buscar codigo
            const http = new XMLHttpRequest();
            http.open("GET", url, true);
            http.send();
            http.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    const res = JSON.parse(this.responseText);
                    if (res) {
                        // POR SI SE QUERIA MOSTRA EL NOMBRE Y PRECIO, SE PUEDE USAR PARA OTROS PROYECTOS INTERESANTES :)
                        document.getElementById("empleado").value = res.nombre + ' ' + res.apellido;
                        document.getElementById("id").value = res.id;
                        document.getElementById("empleado").removeAttribute("disabled"); //Para remover un atributo, por ejemplo el disabled u otro atributo
                        document.getElementById("empleado").focus();
                    } else {
                        alertas('El empleado no existe', 'warning', 'Error');
                        document.getElementById("dni").value = "";
                        document.getElementById("empleado").value = "";
                        // PARA VOLVER A DESABILITAR EL INPUT DE EMLPEADO
                        document.getElementById("empleado").setAttribute("disabled", "disabled"); //Para agregar un atributo, por ejemplo el disabled u otro atributo
                        document.getElementById("dni").focus();
                    }
                }
            }
        }
    } else {
        alertas('Ingrese el DNI del empleado', 'info', 'Info'); //Alerta con toastr
    }
}

// FUNCION PARA GUARDAR HORARIO DE EMPLEADOS
function asignarHorario() {
    const horarioSeleccionado = document.querySelector('input[name="turno"]:checked');
    const id_empleado = document.getElementById('id');
    const diasCheckboxes = document.querySelectorAll('#contenedor-dias input[type="checkbox"]:checked'); //TENER EN CUENTA QUE USAMOS NUMEROS PARA LOS DIAS

    const dni = document.getElementById('dni'); //Para limpiar el input de busqueda de empleado
    const empleado = document.getElementById('empleado');

    const diasSeleccionados = Array.from(diasCheckboxes).map(cb => cb.value);

    // console.log('Empleado '+ id_empleado.value);
    // console.log('horario '+ horarioSeleccionado.value);
    // console.log('Dias seleccionados:', diasSeleccionados);

    // Validación
    if (!horarioSeleccionado || !id_empleado || diasSeleccionados.length === 0) {
        alertas('Seleccionar almenos un Horario, Empleado y los Dias a Asistir', 'warning', 'Info');
        return;
    }

    // Crear FormData
    const datos = new FormData();
    datos.append("id_empleado", id_empleado.value);
    datos.append("id_horario", horarioSeleccionado.value);
    // datos.append("bloque", bloqueSeleccionado.value);
    diasSeleccionados.forEach(dia => {
        datos.append("dias[]", dia);
    });

    const url = BASE_URL + "Horario/registrarHorario";
    const http = new XMLHttpRequest();
    http.open("POST", url, true);
    http.send(datos);
    http.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            // console.log(this.responseText);
            const res = JSON.parse(this.responseText);
            alertas(res.msg, res.icono, res.titulo);

            // limpiar campos
            dni.value = '';
            empleado.value = '';
            id_empleado.value = '';

            // limpiar turno seleccionado
            const horarioSeleccionado = document.querySelector('input[name="turno"]:checked');
            if (horarioSeleccionado) {
                horarioSeleccionado.checked = false;
            }

            // limpiar todos los checkboxes de días
            document.querySelectorAll('#contenedor-dias input[type="checkbox"]')
                .forEach(cb => cb.checked = false);

            // volver a deshabilitar el input de empleado
            empleado.setAttribute("disabled", "disabled");
            // volver a habilitar el input de DNI
            dni.focus();
        }
    };
}