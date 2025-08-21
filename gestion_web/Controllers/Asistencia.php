<?php

class Asistencia extends Controller
{

    public function __construct()
    {
        session_start();
        parent::__construct();
    }

    public function index()
    {
        $id_usuario = $_SESSION['id_usuario'];
        if ($id_usuario) {
            $data['empleados'] = $this->model->getEmpleados();
            $data['asistencias'] = $this->model->obtenerAsistenciaEmpleado();
            $data['horarios'] = $this->model->obtenerHorarioEmpleado();
            $data['mes'] = isset($_GET['mes']) ? (int)$_GET['mes'] : (int)date('m');
            $data['anio'] = isset($_GET['anio']) ? (int)$_GET['anio'] : (int)date('Y');
            $data['dias_en_mes'] = cal_days_in_month(CAL_GREGORIAN, $data['mes'], $data['anio']);
            
            $this->views->getView($this, "index", $data);
        } else {
            header("Location: " . BASE_URL);
        }
    }
}
