<?php
include "Views/template/head.php";
?>
<!-- Sidebar Start -->
<?php
include "Views/template/aside.php";
?>
<!--  Sidebar End -->
<!--  Main wrapper -->

<!--  Header End -->
<div class="container-fluid">

    <div class="card bg-info-subtle shadow-none position-relative overflow-hidden mb-4">
        <div class="card-body px-4 py-3">
            <div class="row align-items-center">
                <div class="col-9">
                    <h4 class="fw-semibold mb-8">Asignacion de Horario</h4>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item">
                                <a class="text-muted text-decoration-none" href="<?= BASE_URL; ?>Administracion/home">Inicio</a>
                            </li>
                            <li class="text-gray breadcrumb-item" aria-current="page">Asignacion de Horario</li>
                        </ol>
                    </nav>
                </div>
                <div class="col-3">
                    <div class="text-center mb-n5">
                        <img src="<?= BASE_URL ?>Assets/img/ChatBc.png" alt="modernize-img" class="img-fluid mb-n4">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-lg-12">
            <!-- start Info Border with Icons -->
            <div class="card">
                <div class="card-body">
                    <h4 class="card-title">Buscar Empleado</h4>
                    <form>
                        <div class="row">
                            <div class="col-md-4">
                                <input type="text" class="form-control border-1 border-success" placeholder="Ingresar el DNI del Empleado" autocomplete="off" id="dni" name="dni" onkeyup="buscarEmpleado(event)">
                                <span style="font-size:small">Presionar ENTER</span>
                            </div>
                            <div class="col-md-8">
                            <!-- EMPLEADO -->
                                <input type="hidden" id="id" name="id">
                                <input type="text" id="empleado" name="empleado" class="form-control" disabled>
                            </div>
                        </div>
                        <div class="mb-3 has-success">
                            <!-- <input type="text" class="form-control"> -->
                            <!-- <select name="empleado" id="empleado" class="form-select">
                                <?php foreach ($data['empleados'] as $empleado) { ?>
                                    <option value="<?= $empleado['id'] ?>"><?= $empleado['nombre'] ?></option>
                                <?php } ?>
                            </select> -->
                        </div>
                    </form>
                </div>
            </div>
            <!-- end Info Border with Icons -->
        </div>
    </div>

    <div class="row">
        <div class="col-xl-9">
            <div class="row">
                <div class="col-md-12">
                    <div class="card mb-0">
                        <div class="card-body p-4" id="contenedor-dias">
                            <h4 class="card-title">Seleccione los días de la semana</h4>
                            <!-- <p class="card-subtitle">The Power of Friendship</p> -->
                            <div class="row gx-3 mt-4">
                                <div class="d-flex justify-content-between">
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="0" value="0" autocomplete="off">
                                        <div style="font-size:0.95em;">Lunes</div>
                                    </div>
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="1" value="1" autocomplete="off">
                                        <div style="font-size:0.95em;">Martes</div>
                                    </div>
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="2" value="2" autocomplete="off">
                                        <div style="font-size:0.95em;">Miercoles</div>
                                    </div>
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="3" value="3" autocomplete="off">
                                        <div style="font-size:0.95em;">Jueves</div>
                                    </div>
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="4" value="4" autocomplete="off">
                                        <div style="font-size:0.95em;">Viernes</div>
                                    </div>
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="5" value="5" autocomplete="off">
                                        <div style="font-size:0.95em;">Sabado</div>
                                    </div>
                                    <div class="flex-fill text-center">
                                        <input type="checkbox" name="dias[]" id="6" value="6" autocomplete="off">
                                        <div style="font-size:0.95em;">Domingo</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-12 mt-4">
                    <div class="card">
                        <div class="card-body p-4">
                            <h4 class="card-title">Seleccionar los turnos</h4>
                            <!-- <p class="card-subtitle">The Iconic Music of Prince</p> -->
                            <div class="row gx-3 mt-4">
                                <div class="d-flex justify-content-between">

                                    <?php foreach ($data['turnos'] as $turno) { ?>
                                        <div class="flex-fill text-center">
                                            <input type="radio" name="turno" id="turno<?= $turno['id'] ?>" value="<?= $turno['id'] ?>" autocomplete="off">
                                            <br><strong><?= $turno['nombre'] ?></strong><br>
                                            <div style="font-size:0.95em;">Entrada: <?= $turno['hora_entrada'] ?> | Salida: <?= $turno['hora_salida'] ?></div>
                                        </div>
                                    <?php } ?>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-md-6 col-xl-3">
            <div class="card">
                <div class="card-body p-3">
                    <!-- <h5 class="card-title fw-semibold">Seleccionar bloque</h5> -->
                    <!-- <p class="card-subtitle">Based on your preferences</p> -->
                    <div class="mt-12 card p-2 rounded shadow-none border">
                        <div class="d-flex align-items-center">
                            <img src="<?= BASE_URL; ?>Assets/img/blog-img5.jpg" class="rounded" alt="album" width="220">
                        </div>
                    </div>
                    <div class="mt-4 p-2 card rounded shadow-none">
                        <div class="flex-fill text-center">
                            <button onclick="asignarHorario()" class="btn btn-danger">GUARDAR HORARIO</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>

<script src="<?= BASE_URL ?>Assets/js/asignar_horario.js">

</script>

<?php
include "Views/template/footer.php";
?>