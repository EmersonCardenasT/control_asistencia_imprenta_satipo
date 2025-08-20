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

    public function listar_turnos()
    {
        $data = $this->model->getTurnos();
        for ($i=0; $i < count($data); $i++) {
            if ($data[$i]['estado'] == 'activo') {
                $data[$i]['estado'] = '<span class="badge bg-success">Activo</span>';
                $data[$i]['acciones'] = '<div>
                                            <button class="btn btn-success btn-action" type="button" onclick="btnEditarTurno('.$data[$i]['id'].');"><i class="ti ti-pencil"></i></button>
                                            <button class="btn btn-danger btn-action" type="button" onclick="btnEliminarTurno('.$data[$i]['id'].');"><i class="ti ti-trash"></i></button>
                                        </div>';
            }
        }
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function registrar()
    {
        $id = $_POST['id'];
        $turno = $_POST['turno'];
        $hora_entrada = $_POST['hora_entrada'];
        $hora_salida = $_POST['hora_salida'];

        if ($turno == "" || $hora_entrada == "" || $hora_salida == "") {
            $msg = array('msg' => 'Todos los campos son obligatorios', 'icono' => 'warning', 'titulo' => 'Advertencia');
        }else {
            if ($id == "") {
                $data = $this->model->registrarTurno($turno, $hora_entrada, $hora_salida);
                if ($data == "ok") {
                    $msg = array('msg' => 'Turno registrado con exito', 'icono' => 'success', 'titulo' => 'Exito');
                }else{
                    $msg = array('msg' => 'Error al registrar el Turno', 'icono' => 'error', 'titulo' => 'Error');
                }
            }else{
                $data = $this->model->modificarTurno($turno, $hora_entrada, $hora_salida, $id);
                if ($data == "modificado") {
                    $msg = array('msg' => 'Turno actualizado correctamente', 'icono' =>'success', 'titulo' => 'Exito');
                }else{  
                    $msg = array('msg' => 'Error al modificar el Turno', 'icono' => 'error', 'titulo' => 'Error');
                }
            }
        }
        echo json_encode($msg, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function editar(int $id)
    {
        $data = $this->model->editarTurno($id);
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function eliminar(int $id)
    {
        $data = $this->model->eliminarTurno($id);
        if ($data == 1) {
            $msg = array('msg' => 'Turno eliminado', 'icono' => 'success', 'titulo' => 'Exito');
        }else{
            $msg = array('msg' => 'Error al eliminar el Turno', 'icono' => 'error', 'titulo' => 'Error');
        }
        echo json_encode($msg, JSON_UNESCAPED_UNICODE);
        die();
    }

    public function asignar_horario()
    {
        $id_usuario = $_SESSION['id_usuario'];
        if ($id_usuario) {
            $data['turnos'] = $this->model->getTurnos();
            $this->views->getView($this, "asignar_horario", $data);
        }else {
            header("Location: " . BASE_URL);
        }
    }

}

?>