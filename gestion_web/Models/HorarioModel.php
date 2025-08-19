<?php

class HorarioModel extends Query
{

    private $id;

    public function __construct()
    {
        parent::__construct();
    }

    public function getTurnos()
    {
        $sql = "SELECT * FROM turnos";
        $data = $this->selectAll($sql);
        return $data;
    }

    public function registrarTurno(string $turno, string $hora_entrada, string $hora_salida)
    {
        $sql = "INSERT INTO turnos(nombre, hora_entrada, hora_salida) VALUES (?, ?, ?)";
        $datos = array($turno, $hora_entrada, $hora_salida);
        $data = $this->save($sql, $datos);
        if ($data == 1) {
            $res = "ok";
        } else {
            $res = "error";
        }
        return $res;
    }

    public function modificarTurno(string $turno, string $hora_entrada, string $hora_salida, int $id)
    {
        $sql = "UPDATE turnos SET nombre =?, hora_entrada =?, hora_salida =? WHERE id =?";
        $datos = array($turno, $hora_entrada, $hora_salida, $id);
        $data = $this->save($sql, $datos);
        if ($data == 1) {
            $res = "modificado";
        }else{
            $res = "error";
        }
        return $res;
    }

    public function editarTurno(int $id)
    {
        $sql = "SELECT * FROM turnos WHERE id = $id";
        $data = $this->select($sql);
        return $data;
    }

    public function eliminarTurno(int $id)
    {
        $this->id = $id;
        $sql = "DELETE FROM turnos WHERE id = ?";
        $datos = array($this->id);
        $data = $this->save($sql, $datos);
        return $data;
    }

}
