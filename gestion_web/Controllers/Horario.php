<?php

class Horario extends Controller
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
            $this->views->getView($this, "index");
        }else {
            header("Location: " . BASE_URL);
        }
    }

    public function asignar_horario()
    {
        $id_usuario = $_SESSION['id_usuario'];
        if ($id_usuario) {
            $this->views->getView($this, "asignar_horario");
        }else {
            header("Location: " . BASE_URL);
        }
    }

}

?>