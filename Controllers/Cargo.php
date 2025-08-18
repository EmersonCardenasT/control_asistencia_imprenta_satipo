<?php

class Cargo extends Controller
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

    public function listar_cargos()
    {
        $data = $this->model->getCargos();

        for ($i = 0; $i < count($data); $i++) {
            if ($data[$i]['estado'] == 'activo') {
                $data[$i]['estado'] = '<span class="badge bg-success rounded-3 fw-semibold">Activo</span>';
            } else {
                $data[$i]['estado'] = '<span class="badge bg-danger rounded-3 fw-semibold">Inactivo</span>';
            }

            $data[$i]['acciones'] = '
                <button class="btn btn-primary btn-action" onclick="btnEditarCargo(' . $data[$i]['id'] . ')" title="Editar">
                    <i class="ti ti-pencil"></i>
                </button>
                <button class="btn btn-danger btn-action" onclick="btnEliminarCargo(' . $data[$i]['id'] . ')" title="Eliminar">
                    <i class="ti ti-trash"></i>
                </button>
            ';
        }

        // Devolver JSON limpio
        header('Content-Type: application/json');
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        exit;
    }

    public function registrar(){
        $cargo = $_POST['cargo'];
        $id = $_POST['id'];

        if(empty($cargo)) {
            $msg = "Todos los campos son obligatorios";
        }else{

            if($id == ""){
                    $data = $this -> model -> registrarCargo($cargo);
                    if ($data == "ok") {
                        $msg = array('msg' => 'Cargo registrado con exito', 'icono' => 'success', 'titulo' => 'Exito');
                    } else if($data == "existe"){
                        $msg = array('msg' => 'La Cargo ya existe', 'icono' => 'warning', 'titulo' => 'Error');
                    }else{
                        $msg = array('msg' => 'Error al registrar la Cargo', 'icono' => 'error', 'titulo' => 'Error');
                    }
                }
            else{
                $data = $this -> model -> modificarCargo($cargo, $id);
                if ($data == "modificado") {
                    $msg = array('msg' => 'Cargo actualizado correctamente', 'icono' => 'success', 'titulo' => 'Exito');
                }else{
                    $msg = array('msg' => 'Error al modificar la Cargo', 'icono' => 'error', 'titulo' => 'Error');
                }
            }

        }
        echo json_encode($msg, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function editar(int $id)
    {
        $data = $this -> model -> editarCargo($id);
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function eliminar(int $id) {
        $data = $this -> model -> eliminarCargo($id);
        if($data == 1){
            $msg = array('msg' => 'El cargo a sido eliminado', 'icono' => 'success', 'titulo' => 'Exito');
        }else{
            $msg = array('msg' => 'Error al eliminar el Cargo', 'icono' => 'error', 'titulo' => 'Error');
        }
        echo json_encode($msg, JSON_UNESCAPED_UNICODE);
        die();
    }

}
