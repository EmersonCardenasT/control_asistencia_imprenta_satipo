<?php
include "Views/template/head.php";
?>
<!-- Sidebar Start -->
<?php
include "Views/template/aside.php";
?>

<!--  Header End -->
<div class="container-fluid">

    <div class="card bg-success-subtle shadow-none position-relative overflow-hidden mb-4">
        <div class="card-body px-4 py-3">
            <div class="row align-items-center">
                <div class="col-9">
                    <h4 class="fw-semibold mb-8"><?= $empleado = !empty($data['empleado']['nombre'] . ' ' . $data['empleado']['apellido'])
                                                        ?
                                                        $data['empleado']['nombre'] . ' ' . $data['empleado']['apellido']
                                                        : 'Empleado no encontrado';
                                                    ?></h4>
                </div>
            </div>
        </div>
    </div>

    <h3></h3>

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


    <div class="col-lg-12 d-flex align-items-stretch">
        <div class="card w-100">
            <div class="card-body p-4">
                <!-- Título -->
                <div class="row mb-4">
                    <div class="col-12">
                        <h3 class="text-center">Plan de turno de actividad laboral semanal del empleado</h3>
                        <p class="text-center">Empleado: <strong><?= $data['empleado']['nombre'] . ' ' . $data['empleado']['apellido'] ?></strong></p>
                        <!-- <p class="text-center">Date: 01/05/2025 to 07/05/2025</p> -->
                    </div>
                </div>

                <!-- Tabla de turnos -->
                <div class="table-responsive">
                    <table class="table table-bordered text-center">
                        <thead class="bg-primary text-white">
                            <tr>
                                <th>Time/Period</th>
                                <th>Lunes</th>
                                <th>Martes</th>
                                <th>Miércoles</th>
                                <th>Jueves</th>
                                <th>Viernes</th>
                                <th class="bg-info">Sábado</th>
                                <th class="bg-danger">Domingo</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                            $horas = [
                                "05:00 AM - 06:00 AM",
                                "06:00 AM - 07:00 AM",
                                "07:00 AM - 08:00 AM",
                                "08:00 AM - 09:00 AM",
                                "09:00 AM - 10:00 AM",
                                "10:00 AM - 11:00 AM",
                                "11:00 AM - 12:00 PM",
                                "12:00 PM - 01:00 PM",
                                "01:00 PM - 02:00 PM",
                                "02:00 PM - 03:00 PM",
                                "03:00 PM - 04:00 PM",
                                "04:00 PM - 05:00 PM",
                                "05:00 PM - 06:00 PM",
                                "06:00 PM - 07:00 PM",
                                "07:00 PM - 08:00 PM",
                                "08:00 PM - 09:00 PM",
                                "09:00 PM - 10:00 PM",
                                "10:00 PM - 11:00 PM",
                                "11:00 PM - 12:00 AM"
                            ];

                            $diasSemana = [
                                0 => "Lunes",
                                1 => "Martes",
                                2 => "Miércoles",
                                3 => "Jueves",
                                4 => "Viernes",
                                5 => "Sábado",
                                6 => "Domingo"
                            ];

                            $turnosPorDia = [];
                            foreach ($data['turnos_empleado'] as $turno) {
                                $turnosPorDia[$turno['dia_semana']][] = [
                                    'entrada' => $turno['hora_entrada'],
                                    'salida'  => $turno['hora_salida']
                                ];
                            }

                            foreach ($horas as $hora) {
                                echo "<tr>";
                                echo "<td class='bg-light'>$hora</td>";

                                // Separar inicio y fin del rango actual
                                [$horaInicioStr, $horaFinStr] = explode(' - ', $hora);
                                $horaInicio = DateTime::createFromFormat('h:i A', $horaInicioStr);

                                for ($i = 0; $i <= 6; $i++) {
                                    $asignado = false;
                                
                                    if (isset($turnosPorDia[$i])) {
                                        foreach ($turnosPorDia[$i] as $rango) {
                                            $entrada = DateTime::createFromFormat('H:i:s', $rango['entrada']);
                                            $salida  = DateTime::createFromFormat('H:i:s', $rango['salida']);
                                
                                            if ($horaInicio >= $entrada && $horaInicio < $salida) {
                                                $asignado = true;
                                                break;
                                            }
                                        }
                                    }
                                
                                    if ($asignado) {
                                        echo "<td class='bg-success text-white'>Asignado</td>";
                                    } else {
                                        echo "<td class='text-muted'>-</td>";
                                    }
                                }
                                
                                echo "</tr>";
                            }
                            ?>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>

</div>

<script src="<?= BASE_URL; ?>Assets/js/empleado.js"></script>

<?php
include "Views/template/footer.php";
?>