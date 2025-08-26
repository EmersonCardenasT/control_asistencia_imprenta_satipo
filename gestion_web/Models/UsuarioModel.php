<?php

class UsuarioModel extends Query
{

    public function __construct()
    {
        parent::__construct();
    }

    public function getUsuario(string $usuario, string $password)
    {
        $sql = "SELECT * FROM usuarios WHERE usuario = '$usuario' AND password = '$password'";
        $data = $this->select($sql);
        return $data;
    }

}
