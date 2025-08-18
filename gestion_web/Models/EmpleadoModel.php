<?php

class EmpleadoModel extends Query
{
    private $id;
    private $nombre;
    private $apellido;
    private $dni;
    private $telefono;
    private $genero;
    private $fecha_nacimiento;
    private $direccion;
    private $estado;
    private $email;
    private $cargo;
    private $id_cargo;
    private $img;

    public function __construct()
    {
        parent::__construct();
    }

    public function getEmpleados()
    {
        $sql = "SELECT e.*, c.nombre as cargo FROM empleados e INNER JOIN cargos c ON c.id = e.cargo_id";
        $data = $this->selectAll($sql);
        return $data;
    }

    public function putModificarEmpleado(string $nombre, string $apellido, string $dni, string $telefono, string $genero, string $fecha_nacimiento, string $direccion, string $email, string $cargo, string $estado, int $id)
    {
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->dni = $dni;
        $this->telefono = $telefono;
        $this->genero = $genero;
        $this->fecha_nacimiento = $fecha_nacimiento;
        $this->direccion = $direccion;
        $this->email = $email;
        $this->cargo = $cargo;
        $this->estado = $estado;
        $this->id = $id;

        $sql = "UPDATE empleados SET nombre = ?, apellido = ?, dni = ?, telefono = ?, direccion = ?, genero = ?, fecha_nacimiento = ?, 
                direccion = ?, email = ?, cargo_id = ?, estado = ? WHERE id = ?";
        $datos = array($this->nombre, $this->apellido, $this->dni, $this->telefono, $this->direccion, $this->genero, $this->fecha_nacimiento,
                $this->direccion, $this->email, $this->cargo, $this->estado, $this->id);
        $data = $this->save($sql, $datos);

        if ($data == 1) {
            $res = "modificado";
        } else {
            $res = "error";
        }

        return $res;
    }

    public function getCargo()
    {
        $sql = "SELECT * FROM cargos WHERE estado = 1";
        $data = $this->selectAll($sql);
        return $data;
    }

    public function editarEmpleado($id)
    {
        $sql = "SELECT * FROM empleados WHERE id = $id";
        $data = $this->select($sql);
        return $data;
    }

    public function eliminarEmpleado(int $id)
    {
        $this->id = $id;
        $sql = "DELETE FROM empleados WHERE id = ?";
        $datos = array($this->id);
        $data = $this->save($sql, $datos);
        return $data;
    }

}
