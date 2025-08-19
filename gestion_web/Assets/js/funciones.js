function initDataTable(selector, url, columnas, order = [[0, 'desc']]) {
    // Evitar re-inicialización
    if ($.fn.DataTable.isDataTable(selector)) {
        $(selector).DataTable().destroy();
    }

    return $(selector).DataTable({
        ajax: {
            url: url,
            dataSrc: ''
        },
        columns: columnas,
        order: order,
        responsive: true,
        language: getLenguajeData()
    });
}

document.addEventListener("DOMContentLoaded", function () {
    // Cargo
    tblCargo = initDataTable("#tblCargo", BASE_URL + "Cargo/listar_cargos", [
        { data: 'id' },
        { data: 'nombre' },
        { data: 'estado' },
        { data: 'created_at' },
        { data: 'acciones' }
    ]);

    // EMPLEADOS
    tblEmpleado = initDataTable("#tblEmpleado", BASE_URL + "Empleado/listar_empleados", [
        { data: 'id' },
        {
            data: null, // 👈 usamos toda la fila
            render: function(data, type, row) {
                return `
                    <div class="d-flex align-items-center">
                        <img src="${BASE_URL + row.foto}" 
                             class="rounded-circle me-2" 
                             width="45" height="45">
                        <span>${row.nombre} ${row.apellido}</span>
                    </div>
                `;
            }
        },
        { data: 'cargo' },
        { data: 'estado' },
        { data: 'created_at' },
        { data: 'acciones' }
    ]);

    // TURNOS
    tblTurnos = initDataTable("#tblTurnos", BASE_URL + "Horario/listar_turnos", [
        { data: 'id' },
        { data: 'nombre' },
        { data: 'hora_entrada' },
        { data: 'hora_salida' },
        { data: 'estado' },
        { data: 'created_at' },
        { data: 'acciones' }
    ]);
});

function getLenguajeData() {
    return {
        "decimal": "",
        "emptyTable": "No hay información",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
        "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
        "infoFiltered": "(Filtrado de _MAX_ total entradas)",
        "infoPostFix": "",
        "thousands": ",",
        "lengthMenu": "Mostrar _MENU_ Entradas",
        "loadingRecords": "Cargando...",
        "processing": "Procesando...",
        "search": "Buscar:",
        "zeroRecords": "Sin resultados encontrados",
        "paginate": {
            "first": "Primero",
            "last": "Ultimo",
            "next": "Siguiente",
            "previous": "Anterior"
        }
    }
}

// FUNCION PARA LAS ALERTAS
function alertas(mensaje, icono, titulo) {
    Swal.fire({
        title: titulo,
        text: mensaje,
        icon: icono,
        timer: 2500
    });
}

function alertaToastSuccess(mensaje, titulo) {
    toastr.success(mensaje, titulo); //Alerta con toastr
}
// FIN DE ALERTAS

