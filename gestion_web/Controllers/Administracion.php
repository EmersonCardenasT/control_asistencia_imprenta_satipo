<?php

class Administracion extends Controller
{

    public function __construct()
    {
        session_start();

        // // Tiempo máximo de inactividad (ej. 15 minutos)
        // $tiempo_maximo = 500;

        // if (empty($_SESSION['activo'])) {
        //     header("Location: " . BASE_URL);
        //     exit;
        // }

        // // Verificar inactividad
        // if (isset($_SESSION['ultima_actividad']) && (time() - $_SESSION['ultima_actividad'] > $tiempo_maximo)) {
        //     // Se pasó el tiempo, destruir sesión
        //     session_unset();
        //     session_destroy();
        //     header("Location: " . BASE_URL . "Usuarios/salir"); // Redirecciona al logout o login
        //     exit;
        // }

        // // Actualizar tiempo de última actividad
        // $_SESSION['ultima_actividad'] = time();

        parent::__construct();
    }

    // public function index()
    // {
    //     $id_usuario = $_SESSION['id_usuario'];
    //     $verificar = $this->model->verificarPermiso($id_usuario, 'configuracion');
    //     if (!empty($verificar) || $id_usuario == usuario_administrador) {
    //         $data = $this->model->getEmpresa();
    //         $this->views->getView($this, "index", $data); //La $data le pasamos a la vista
    //     } else {
    //         header('Location: ' . BASE_URL . 'Errors/permisos');
    //     }
    // }

    public function home()
    {
        $id_usuario = $_SESSION['id_usuario'];
        if ($id_usuario) {
            $this->views->getView($this, "home"); //, $data
        }else {
            header("Location: " . BASE_URL);
        }
    }

    
}
