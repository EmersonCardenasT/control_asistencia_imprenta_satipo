<?php

class AsistenciaModel extends Query
{

    public function __construct()
    {
        parent::__construct();
    }

    // METODO PARA LISTAR EMPLEADOS
    public function getEmpleados()
    {
        $sql = "SELECT e.*, ec.fecha_inicio as inicio_actividades FROM empleados e INNER JOIN empleado_contrato ec ON e.id = ec.empleado_id";
        $data = $this->selectAll($sql);
        return $data;
    }

    // METODO PARA OBTENER LA ASISTENCIA DE LOS EMPLEADOS
    public function obtenerAsistenciaEmpleado()
    {
        $sql = "SELECT e.id AS empleado_id, CONCAT(e.nombre, ' ' , e.apellido) as Empleado, a.fecha, a.hora_entrada, 
        a.hora_salida, a.bloque, a.minutos_tarde, a.estado from asistencia a 
        INNER JOIN empleados e ON e.id = a.empleado_id";
        $data = $this->selectAll($sql);
        return $data;
    }

    // METODO PARA OBTENER LOS DIAS QUE LOS EMPLEADOS TIENEN QUE ASISTIR    
    public function obtenerHorarioEmpleado()
    {
        $sql = "SELECT 
                    e.id AS empleado_id,
                    CONCAT(e.nombre, ' ', e.apellido) AS empleado,
                    t.nombre AS horario,
                    CASE 
                        WHEN te.dia_semana = 0 THEN 1
                        WHEN te.dia_semana = 1 THEN 2
                        WHEN te.dia_semana = 2 THEN 3
                        WHEN te.dia_semana = 3 THEN 4
                        WHEN te.dia_semana = 4 THEN 5
                        WHEN te.dia_semana = 5 THEN 6
                        WHEN te.dia_semana = 6 THEN 7
                    END AS dia_numero
                FROM empleados e
                INNER JOIN turnos_empleado te ON e.id = te.empleado_id
                INNER JOIN turnos t ON t.id = te.turno_id
                ORDER BY e.id, dia_numero;";
        $data = $this->selectAll($sql);
        return $data;
    }

}
