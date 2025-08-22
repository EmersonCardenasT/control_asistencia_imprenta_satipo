<?php
include "Views/template/head.php";

// Configurar localización en español
setlocale(LC_TIME, 'es_ES.UTF-8');

// Variables recibidas desde el controlador
$empleados = $data['empleados'];
$asistencias = $data['asistencias'];
$horarios = $data['horarios'];
$mes = $data['mes'];
$anio = $data['anio'];
// $dias_en_mes = cal_days_in_month(CAL_GREGORIAN, $mes, $anio);
$dias_en_mes = $data['dias_en_mes'];

// Semana actual (viene por GET o por defecto 1)
$semana = isset($_GET['semana']) ? (int)$_GET['semana'] : 1;

// Procesar las asistencias por empleado y día
$asistencias_por_empleado = [];
foreach ($asistencias as $registro) {
    $empleado_id = $registro['empleado_id'];
    $fecha = new DateTime($registro['fecha']);
    $mesRegistro = (int)$fecha->format('n');
    $anioRegistro = (int)$fecha->format('Y');

    if ($mesRegistro === (int)$mes && $anioRegistro === (int)$anio) {
        $dia = (int)$fecha->format('j');
        $asistencias_por_empleado[$empleado_id][$dia] = $registro;
    }
}

// Procesar los horarios por empleado y día de la semana
$horarios_por_empleado = [];
foreach ($horarios as $horario) {
    $empleado_id = $horario['empleado_id'];
    $dia_semana = $horario['dia_numero']; // Ya lo tienes en número
    $horarios_por_empleado[$empleado_id][$dia_semana] = $horario['horario'];
}


// Crear formateadores de fechas en español
$formatter_dia = new IntlDateFormatter('es_ES', IntlDateFormatter::FULL, IntlDateFormatter::NONE);
$formatter_dia->setPattern('EEEE');

$formatter_mes = new IntlDateFormatter('es_ES', IntlDateFormatter::FULL, IntlDateFormatter::NONE);
$formatter_mes->setPattern('MMMM');

// Calcular el rango de días de la semana actual
$maxSemanas = (int)ceil($dias_en_mes / 7);
$semana = max(1, min($semana, $maxSemanas)); // Limitar rango de semana válido
$inicioDia = ($semana - 1) * 7 + 1;
$finDia = min($inicioDia + 6, $dias_en_mes);

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
                    <h4 class="fw-semibold mb-8">CONTROL DE ASISTENCIA</h4>
                    <nav aria-label="breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item">
                                <a class="text-muted text-decoration-none" href="<?= BASE_URL; ?>Administracion/home">Inicio</a>
                            </li>
                            <li class="text-gray breadcrumb-item" aria-current="page">Control de asistencia</li>
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

    
    <section class="content">
        <div class="container-fluid">
            <div class="card">
                <div class="card-body">
                    <!-- Filtros de mes y año -->
                    <form method="GET" class="mb-3">
                        <select name="mes" class="form-control d-inline w-auto">
                            <?php for ($m = 1; $m <= 12; $m++): ?>
                                <option value="<?php echo $m; ?>" <?php echo $m == $mes ? 'selected' : ''; ?>>
                                    <?php
                                    $fecha_mes = new DateTime("$anio-$m-01");
                                    echo ucfirst($formatter_mes->format($fecha_mes));
                                    ?>
                                </option>
                            <?php endfor; ?>
                        </select>
                        <select name="anio" class="form-control d-inline w-auto">
                            <?php for ($y = 2020; $y <= date('Y'); $y++): ?>
                                <option value="<?php echo $y; ?>" <?php echo $y == $anio ? 'selected' : ''; ?>>
                                    <?php echo $y; ?>
                                </option>
                            <?php endfor; ?>
                        </select>
                        <input type="hidden" name="semana" value="<?php echo $semana; ?>">
                        <button type="submit" class="btn btn-primary">Filtrar</button>
                    </form>

                    <!-- Navegación de semanas -->
                    <div class="mb-3">
                        <?php
                        $fechaInicio = new DateTime("$anio-$mes-$inicioDia");
                        $fechaFin = new DateTime("$anio-$mes-$finDia");
                        $semanaAnterior = max(1, $semana - 1);
                        $semanaSiguiente = min($maxSemanas, $semana + 1);
                        ?>
                        <a href="?mes=<?php echo $mes; ?>&anio=<?php echo $anio; ?>&semana=<?php echo $semanaAnterior; ?>" class="btn btn-secondary">
                            &laquo; Semana anterior
                        </a>
                        <span class="mx-2 font-weight-bold">Semana <?php echo $semana; ?> (<?php echo $fechaInicio->format('d M'); ?> - <?php echo $fechaFin->format('d M'); ?>)</span>
                        <a href="?mes=<?php echo $mes; ?>&anio=<?php echo $anio; ?>&semana=<?php echo $semanaSiguiente; ?>" class="btn btn-secondary">
                            Semana siguiente &raquo;
                        </a>
                    </div>

                    <!-- Tabla de asistencias -->
                    <div class="table-responsive">
                        <table class="table table-bordered text-center">
                            <thead class="thead-dark">
                                <tr>
                                    <th>Nombre</th>
                                    <?php for ($dia = $inicioDia; $dia <= $finDia; $dia++): ?>
                                        <?php
                                        $fecha_actual = new DateTime("$anio-$mes-$dia");
                                        $dia_semana = ucfirst($formatter_dia->format($fecha_actual));
                                        ?>
                                        <th><?php echo $dia . '<br>' . $dia_semana; ?></th>
                                    <?php endfor; ?>
                                    <th>Asistencias</th>
                                    <th>Tardanzas</th>
                                    <th>Ausencias Semanales</th> <!-- Nueva columna para ausencias -->
                                    <th>Ausencias Mensuales</th> <!-- Nueva columna para ausencias -->
                                    <th>% Asistencias Semanal</th>
                                    <th>% Asistencias Mensual</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php foreach ($empleados as $empleado): ?>
                                    <?php
                                    $empleado_id = $empleado['id'];
                                    $nombre = $empleado['nombre'] . ' ' . $empleado['apellido'];
                                    $inicio_actividades = new DateTime($empleado['inicio_actividades']);
                                    $hoy = new DateTime();
                                    $hoy = (clone $hoy)->modify('-1 day');

                                    $conteoAsistencias = 0;
                                    $conteoTardanzas = 0;
                                    ?>
                                    <tr>
                                        <td><?php echo $nombre; ?></td>

                                        <?php for ($dia = $inicioDia; $dia <= $finDia; $dia++): ?>
                                            <td>
                                                <?php
                                                $fecha_actual = new DateTime("$anio-$mes-$dia");

                                                // Si es antes del inicio de actividades o después de hoy, mostrar '-'
                                                if ($fecha_actual < $inicio_actividades || $fecha_actual > $hoy) {
                                                    echo '-';
                                                    continue;
                                                }

                                                $dia_semana = $fecha_actual->format('N');

                                                if (isset($horarios_por_empleado[$empleado_id][$dia_semana])) {
                                                    if (isset($asistencias_por_empleado[$empleado_id][$dia])) {
                                                        $registro = $asistencias_por_empleado[$empleado_id][$dia];
                                                        if ($registro['estado'] !== 'Ausente') {
                                                            $conteoAsistencias++;
                                                            if ($registro['estado'] === 'Tarde') {
                                                                $conteoTardanzas++;
                                                                echo '<i class="fas fa-clock text-warning"></i>';
                                                            } else {
                                                                echo '<i class="fas fa-check text-success"></i>';
                                                            }
                                                        } else {
                                                            echo '<i class="fas fa-times text-danger"></i>';
                                                        }
                                                    } else {
                                                        echo '<i class="fas fa-times text-danger"></i>';
                                                    }
                                                } else {
                                                    echo '-';
                                                }
                                                ?>
                                            </td>
                                        <?php endfor; ?>

                                        <?php
                                        $conteoAusencias = 0;
                                        $diasLaborables = 0;

                                        $conteoAusenciasMensual = 0;
                                        $diasLaborablesMensual = 0;

                                        for ($dia = $inicioDia; $dia <= $finDia; $dia++) {
                                            $fecha_actual = new DateTime("$anio-$mes-$dia");
                                            if ($fecha_actual < $inicio_actividades || $fecha_actual > $hoy) continue;

                                            $dia_semana = $fecha_actual->format('N');

                                            if (isset($horarios_por_empleado[$empleado_id][$dia_semana])) {
                                                $diasLaborables++;
                                                if (isset($asistencias_por_empleado[$empleado_id][$dia])) {
                                                    $registro = $asistencias_por_empleado[$empleado_id][$dia];
                                                    if ($registro['estado'] === 'Ausente') {
                                                        $conteoAusencias++;
                                                    }
                                                } else {
                                                    $conteoAusencias++;
                                                }
                                            }
                                        }

                                        for ($dia = 1; $dia <= $dias_en_mes; $dia++) {
                                            $fecha_actual = new DateTime("$anio-$mes-$dia");
                                            if ($fecha_actual < $inicio_actividades || $fecha_actual > $hoy) continue;

                                            $dia_semana = $fecha_actual->format('N');

                                            if (isset($horarios_por_empleado[$empleado_id][$dia_semana])) {
                                                $diasLaborablesMensual++;
                                                if (isset($asistencias_por_empleado[$empleado_id][$dia])) {
                                                    $registro = $asistencias_por_empleado[$empleado_id][$dia];
                                                    if ($registro['estado'] === 'Ausente') {
                                                        $conteoAusenciasMensual++;
                                                    }
                                                } else {
                                                    $conteoAusenciasMensual++;
                                                }
                                            }
                                        }

                                        $conteoAsistenciasMensual = $diasLaborablesMensual - $conteoAusenciasMensual;
                                        ?>

                                        <td><?php echo $conteoAsistencias; ?></td>
                                        <td><?php echo $conteoTardanzas; ?></td>
                                        <td><?php echo $conteoAusencias; ?></td>
                                        <td><?php echo $conteoAusenciasMensual; ?></td>
                                        <td><?php echo $diasLaborables > 0 ? round(($conteoAsistencias / $diasLaborables) * 100, 2) . '%' : '0%'; ?></td>
                                        <td><?php echo $diasLaborablesMensual > 0 ? round(($conteoAsistenciasMensual / $diasLaborablesMensual) * 100, 2) . '%' : '0%'; ?></td>
                                    </tr>
                                <?php endforeach; ?>
                            </tbody>


                        </table>
                    </div>

                </div>
            </div>
        </div>
    </section>

</div>


<?php
include "Views/template/footer.php";
?>