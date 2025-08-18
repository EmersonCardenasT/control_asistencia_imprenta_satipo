<?php

class Usuario extends Controller
{

    public function __construct()
    {
        session_start();
        parent::__construct();
    }

    public function validar()
    {
        if (empty($_POST['usuario']) || empty($_POST['password'])) {
            $msg = "Los campos estan vacios";
        } else {
            $usuario = $_POST['usuario'];
            $password = $_POST['password'];
            // $hash = hash("SHA256", $password);
            $data = $this->model->getUsuario($usuario, $password); //, $hash   - Agregar despues de $usuario, 
            if ($data) {
                if ($data['estado'] == 1) {
                    $_SESSION['id_usuario'] = $data['id'];
                    $_SESSION['usuario'] = $data['usuario'];
                    $_SESSION['nombre'] = $data['nombre'];
                    $_SESSION['apellido'] = $data['apellido'];
                    $_SESSION['estado'] = $data['estado'];
                    $_SESSION['created_at'] = $data['created_at'];
                    $_SESSION['activo'] = true;
                    $msg = "ok";
                } else {
                    $msg = "Usuario inactivo, por favor contacta al administrador";
                }
            } else {
                $msg = "Usuario o contraseña incorrecta";
            }
        }
        echo json_encode($msg, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function salir()
    {
        session_destroy();
        header("Location: " . BASE_URL);
    }

}

?>