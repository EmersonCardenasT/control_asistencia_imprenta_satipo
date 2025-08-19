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
                    <h4 class="fw-semibold mb-8">GESTION DE PERMISOS</h4>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item">
                                <a class="text-muted text-decoration-none" href="<?= BASE_URL; ?>Administracion/home">Inicio</a>
                            </li>
                            <li class="text-gray breadcrumb-item" aria-current="page">Gestion de Permisos</li>
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
    
</div>


<?php
include "Views/template/footer.php";
?>