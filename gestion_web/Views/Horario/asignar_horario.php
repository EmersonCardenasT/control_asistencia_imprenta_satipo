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
                    <h4 class="card-title">Seleccionar al Empleado</h4>
                    <form>
                        <div class="mb-3 has-success">
                            <select class="form-select">
                                <option value="">Male</option>
                                <option value="">Female</option>
                            </select>
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
                        <div class="card-body p-4">
                            <h4 class="card-title">My Friends</h4>
                            <p class="card-subtitle">The Power of Friendship</p>
                            <div class="row gx-3 mt-4">
                                <div class="col-3">
                                    <img src="../assets/images/profile/user-2.jpg" class="rounded img-fluid" alt="art">
                                </div>
                                <div class="col-3">
                                    <img src="../assets/images/profile/user-3.jpg" class="rounded img-fluid" alt="art">
                                </div>
                                <div class="col-3">
                                    <img src="../assets/images/profile/user-4.jpg" class="rounded img-fluid" alt="art">
                                </div>
                                <div class="col-3">
                                    <img src="../assets/images/profile/user-5.jpg" class="rounded img-fluid" alt="art">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-md-12 mt-4">
                    <div class="card">
                        <div class="card-body p-4">
                            <h4 class="card-title">Favourite Artists</h4>
                            <p class="card-subtitle">The Iconic Music of Prince</p>
                            <div class="row gx-3 mt-4">
                                <div class="col-3">
                                    <img src="../assets/images/music/s1.jpg" class="rounded img-fluid" alt="art">
                                </div>
                                <div class="col-3">
                                    <img src="../assets/images/music/s2.jpg" class="rounded img-fluid" alt="art">
                                </div>
                                <div class="col-3">
                                    <img src="../assets/images/music/s3.jpg" class="rounded img-fluid" alt="art">
                                </div>
                                <div class="col-3">
                                    <img src="../assets/images/music/s4.jpg" class="rounded img-fluid" alt="art">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-md-6 col-xl-3">
            <div class="card">
                <div class="card-body p-4">
                    <h5 class="card-title fw-semibold">Seleccionar bloque</h5>
                    <!-- <p class="card-subtitle">Based on your preferences</p> -->
                    <div class="mt-4 card p-3 rounded shadow-none border">
                        <div class="d-flex align-items-center">
                            <div class="position-relative">
                                TURNO TEMPRANO
                            </div>
                        </div>
                    </div>
                    <div class="mt-4 card p-3 rounded shadow-none border">
                        <div class="d-flex align-items-center">
                            <div class="position-relative">
                                TURNO TARDE
                            </div>
                        </div>
                    </div>
                    <div class="mt-4 card p-3 rounded shadow-none border">
                        <div class="d-flex align-items-center">
                            <div class="position-relative">
                                TURNO NOCHE
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

</div>


<?php
include "Views/template/footer.php";
?>