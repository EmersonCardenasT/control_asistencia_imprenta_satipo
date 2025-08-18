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

    <h3>GESTION DE CARGOS</h3>

    <div class="col-lg-12 d-flex align-items-stretch">
        <div class="card w-100">
            <div class="card-body p-4">

                <button class="btn btn-primary m-1 mb-4" type="button" onclick="frmCargo();">
                    Registrar cargo
                </button>

                <div class="table-responsive">
                    <table class="table text-nowrap mb-0 align-middle" id="tblCargo">
                        <thead class="text-dark fs-4">
                            <tr>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Id</h6>
                                </th>
                                <th class="border-bottom-0">
                                    <h6 class="fw-semibold mb-0">Nombre</h6>
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

                <div id="nuevo_cargo" class="modal fade" tabindex="-1" role="dialog" aria-labelledby="my-modal-title" aria-hidden="true">
                    <div class="modal-dialog" role="document">
                        <div class="modal-content">
                            <div class="modal-header bg-primary">
                                <h5 class="modal-title text-white" id="title">Nuevo Cargo</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <!-- Form -->
                                <form id="frmCargo" method="post" autocomplete="off">
                                    <div class="modal-body">
                                        <input type="hidden" name="id" id="id">
                                        <div class="form-group">
                                            <label for="cargo" class="mb-1">Cargo</label>
                                            <input id="cargo" name="cargo" type="text" class="form-control" placeholder="Ingrese cargo" required>
                                        </div>
                                    </div>
                                    
                                    <!-- Footer -->
                                    <div class="modal-footer">
                                        <button type="button" class="btn bg-danger-subtle text-danger  waves-effect" data-bs-dismiss="modal">Cancelar</button>
                                        <button type="button" class="btn btn-primary" id="btnAccion" onclick="registrarCargo(event);">
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


<!-- SCRIPT PARA CARGOS -->
<script src="<?= BASE_URL; ?>Assets/js/cargo.js"></script>

<?php
include "Views/template/footer.php";
?>