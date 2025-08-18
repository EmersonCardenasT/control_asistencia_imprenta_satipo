<?php

class CargoModel extends Query
{

    private $cargo, $id, $estado;

    public function __construct()
    {
        parent::__construct();
    }

    public function getCargos()
    {
        $sql = "SELECT * FROM cargos";
        $data = $this->selectAll($sql);
        return $data;
    }

    public function registrarCargo(string $cargo)
    {
        $this->cargo = $cargo;

        $sql = "INSERT INTO cargos(nombre) VALUES (?)";
        $datos = array($this->cargo);
        $data = $this->save($sql, $datos);

        if ($data == 1) {
            $res = "ok";
        } else {
            $res = "error";
        }

        return $res;
    }

    public function modificarCargo(string $cargo, int $id)
    {
        $this->cargo = $cargo;
        $this->id = $id;

        $sql = "UPDATE cargos SET nombre = ? WHERE id = ?";
        $datos = array($this->cargo, $this->id);
        $data = $this->save($sql, $datos);

        if ($data == 1) {
            $res = "modificado";
        } else {
            $res = "error";
        }

        return $res;
    }

    public function editarCargo(int $id)
    {
        $sql = "SELECT * FROM cargos WHERE id = $id";
        $data = $this->select($sql);
        return $data;
    }

    public function eliminarCargo(int $id)
    {
        $this->id = $id;
        $sql = "DELETE FROM cargos WHERE id = ?";
        $datos = array($this->id);
        $data = $this->save($sql, $datos);
        return $data;
    }
}
