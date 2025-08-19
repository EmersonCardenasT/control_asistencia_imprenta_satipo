<?php
include "Views/template/head.php";
?>
<!-- Sidebar Start -->
<?php
include "Views/template/aside.php";
?>

<!--  Header End -->
<div class="container-fluid">

    <h3><?= $empleado = !empty($data['empleado']['nombre'] . ' ' . $data['empleado']['apellido']) 
                        ? 
                        $data['empleado']['nombre'] . ' ' . $data['empleado']['apellido'] 
                        : 'Empleado no encontrado'; 
    ?></h3> 

    <div class="col-lg-12 d-flex align-items-stretch">
    <div class="card w-100">
        <div class="card-body p-4">
            <div class="row">
                <!-- Columna de la Foto -->
                <div class="col-md-4 text-center">
                    <img src="https://www.dzoom.org.es/wp-content/uploads/2016/12/tipos-de-plano-cabecera-ok-810x540.jpg"
                         alt="Foto Empleado"
                         class="img-fluid rounded-circle mb-3"
                         style="width: 200px; height: 200px; object-fit: cover; border: 4px solid #eee;">

                    <!-- Fecha de creación debajo de la foto -->
                    <p class="mt-3 text-muted">
                        <strong>Fecha de Creación:</strong><br>
                        <?= !empty($data['empleado']['created_at']) 
                            ? date('d/m/Y H:i', strtotime($data['empleado']['created_at'])) 
                            : '-'; ?>
                    </p>
                </div>

                <!-- Columna de los Datos (divididos en dos columnas) -->
                <div class="col-md-8">
                    <div class="row">
                        <!-- Columna izquierda -->
                        <div class="col-md-6">
                            <table class="table table-borderless mb-0">
                                <tbody>
                                    <tr>
                                        <th class="text-end">Nombre:</th>
                                        <td><?= !empty($data['empleado']['nombre']) ? $data['empleado']['nombre'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Apellido:</th>
                                        <td><?= !empty($data['empleado']['apellido']) ? $data['empleado']['apellido'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">DNI:</th>
                                        <td><?= !empty($data['empleado']['dni']) ? $data['empleado']['dni'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Teléfono:</th>
                                        <td><?= !empty($data['empleado']['telefono']) ? $data['empleado']['telefono'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Género:</th>
                                        <td>
                                            <?php 
                                                if (!empty($data['empleado']['genero'])) {
                                                    echo $data['empleado']['genero'] == 'M' ? 'Masculino' : ($data['empleado']['genero'] == 'F' ? 'Femenino' : 'Otro');
                                                } else {
                                                    echo '-';
                                                }
                                            ?>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- Columna derecha -->
                        <div class="col-md-6">
                            <table class="table table-borderless mb-0">
                                <tbody>
                                    <tr>
                                        <th class="text-end">Fecha Nacimiento:</th>
                                        <td><?= !empty($data['empleado']['fecha_nacimiento']) ? date('d/m/Y', strtotime($data['empleado']['fecha_nacimiento'])) : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Dirección:</th>
                                        <td><?= !empty($data['empleado']['direccion']) ? $data['empleado']['direccion'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Email:</th>
                                        <td><?= !empty($data['empleado']['email']) ? $data['empleado']['email'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Cargo:</th>
                                        <td><?= !empty($data['empleado']['cargo']) ? $data['empleado']['cargo'] : '-'; ?></td>
                                    </tr>
                                    <tr>
                                        <th class="text-end">Estado:</th>
                                        <td>
                                            <?php
                                                if (isset($data['empleado']['estado'])) {
                                                    echo $data['empleado']['estado'] == 'activo' 
                                                        ? '<span class="badge bg-success">Activo</span>' 
                                                        : '<span class="badge bg-danger">Inactivo</span>';
                                                } else {
                                                    echo '-';
                                                }
                                            ?>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div> <!-- /row -->
                </div> <!-- /col-md-8 -->
            </div> <!-- /row -->
        </div>
    </div>
</div>


</div>

<script src="<?= BASE_URL; ?>Assets/js/empleado.js"></script>

<?php
include "Views/template/footer.php";
?>