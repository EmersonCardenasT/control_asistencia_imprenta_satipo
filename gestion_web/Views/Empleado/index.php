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
                    <h4 class="fw-semibold mb-8">GESTION DE EMPLEADOS</h4>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item">
                                <a class="text-muted text-decoration-none" href="<?= BASE_URL; ?>Administracion/home">Inicio</a>
                            </li>
                            <li class="text-gray breadcrumb-item" aria-current="page">Gestion de empleados</li>
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

    <div class="col-lg-12 d-flex align-items-stretch">
        <div class="card w-100">
            <div class="card-body p-4">

                <div class="table-responsive">
                    <table class="table text-nowrap mb-0 align-middle" id="tblEmpleado">
                        <thead class="text-dark fs-4">
                            <tr>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Id</h6>
                                </th>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Empleado</h6>
                                </th>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Cargo</h6>
                                </th>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Estado</h6>
                                </th>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Created at</h6>
                                </th>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Acciones</h6>
                                </th>
                            </tr>
                        </thead>
                        <tbody>

                        </tbody>
                    </table>
                </div>

                <div id="modificar_empleado" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="my-modal-title" aria-hidden="true">
                    <div class="modal-dialog modal-lg" role="document">
                        <div class="modal-content">
                            <div class="modal-header bg-primary">
                                <h5 class="modal-title text-white" id="title">Modificar Empleado</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <!-- Form -->
                                <form id="frmEmpleado" method="post" autocomplete="off">
                                    <div class="modal-body">
                                        <input type="hidden" name="id" id="id">

                                        <div class="row">
                                            <!-- Nombre -->
                                            <div class="form-group col-md-6">
                                                <label for="nombre" class="mb-1">Nombre</label>
                                                <input id="nombre" name="nombre" type="text" class="form-control" placeholder="Ingrese nombre" required>
                                            </div>

                                            <!-- Apellido -->
                                            <div class="form-group col-md-6">
                                                <label for="apellido" class="mb-1">Apellido</label>
                                                <input id="apellido" name="apellido" type="text" class="form-control" placeholder="Ingrese apellido" required>
                                            </div>

                                            <!-- DNI -->
                                            <div class="form-group col-md-5">
                                                <label for="dni" class="mb-1">DNI</label>
                                                <input id="dni" name="dni" type="text" class="form-control" placeholder="Ingrese DNI" required>
                                            </div>

                                            <!-- Teléfono -->
                                            <div class="form-group col-md-6">
                                                <label for="telefono" class="mb-1">Teléfono</label>
                                                <input id="telefono" name="telefono" type="text" class="form-control" placeholder="Ingrese teléfono" required>
                                            </div>

                                            <!-- Género -->
                                            <div class="form-group col-md-6">
                                                <label for="genero" class="mb-1">Género</label>
                                                <select id="genero" name="genero" class="form-control" required>
                                                    <option value="">Seleccione género</option>
                                                    <option value="M">Masculino</option>
                                                    <option value="F">Femenino</option>
                                                </select>
                                            </div>

                                            <!-- Fecha de nacimiento -->
                                            <div class="form-group col-md-6">
                                                <label for="fecha_nacimiento" class="mb-1">Fecha de nacimiento</label>
                                                <input id="fecha_nacimiento" name="fecha_nacimiento" type="date" class="form-control" required>
                                            </div>

                                            <!-- Dirección -->
                                            <div class="form-group col-md-7">
                                                <label for="direccion" class="mb-1">Dirección</label>
                                                <input id="direccion" name="direccion" type="text" class="form-control" placeholder="Ingrese dirección" required>
                                            </div>

                                            <!-- Email -->
                                            <div class="form-group col-md-5">
                                                <label for="email" class="mb-1">Email</label>
                                                <input id="email" name="email" type="email" class="form-control" placeholder="Ingrese email" required>
                                            </div>

                                            <!-- Cargo -->
                                            <div class="form-group col-md-6">
                                                <label for="cargos" class="mb-1">Cargo</label>
                                                <select id="cargos" name="cargos" class="form-control" required>
                                                    <?php foreach ($data['cargos'] as $row) { ?>
                                                        <option value="<?= $row['id']; ?>"><?= $row['nombre']; ?></option>
                                                    <?php } ?>
                                                </select>
                                            </div>

                                            <!-- Estado -->
                                            <div class="form-group col-md-6">
                                                <label for="estado" class="mb-1">Estado</label>
                                                <select id="estado" name="estado" class="form-control" required>
                                                    <option value="activo">Activo</option>
                                                    <option value="inactivo">Inactivo</option>
                                                </select>
                                            </div>

                                        </div>
                                    </div>

                                    <!-- Footer -->
                                    <div class="modal-footer">
                                        <button type="button" class="btn bg-danger-subtle text-danger" data-bs-dismiss="modal">Cancelar</button>
                                        <button type="button" class="btn btn-primary" id="btnAccion" onclick="modificarEmpleado(event);">
                                            Registrar
                                        </button>
                                    </div>
                                </form>

                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

</div>

<script src="<?= BASE_URL; ?>Assets/js/empleado.js"></script>

<?php
include "Views/template/footer.php";
?>