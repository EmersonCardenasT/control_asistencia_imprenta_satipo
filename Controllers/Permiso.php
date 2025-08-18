<?php

class Permiso extends Controller
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
        }
    }

}

?>