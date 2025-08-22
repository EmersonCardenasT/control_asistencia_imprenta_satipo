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
            $data['empleados'] = $this->model->getEmpleados();
            $data['turnos'] = $this->model->getTurnos();
            $this->views->getView($this, "asignar_horario", $data);
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

    // REGISTRAR NUEVO HORARIO PARA EL EMPLEADO
     // Metodo para registrar el horario de un empleado y verificar si ya tiene horario asignado
     public function registrarHorario()
     {
         $empleado = $_POST['id_empleado'];
         $horario = $_POST['id_horario'];
         $dias = $_POST['dias']; // esto es un array
        //  $bloque = $_POST['bloque'];
 
         if (empty($empleado) || empty($horario) || empty($dias)) {
             $msg = array('msg' => 'Todos los campos son obligatorios', 'icono' => 'error', 'titulo' => 'Error');
         } else {
             $conflictos = [];
 
             foreach ($dias as $dia) {
                 // Verifica si el empleado ya tiene un horario asignado en ese día (sin importar cuál)
                 $verificar = $this->model->verificarHorarioPorDia($empleado, $dia);
                 if (!empty($verificar)) {
                     $turnoNombre = $verificar['nombre_turno'] ?? 'desconocido';
                     $conflictos[] = "$dia ($turnoNombre)";
                 }
             }
 
             if (!empty($conflictos)) {
                 $lista = implode(', ', $conflictos);
                 $msg = array(
                     'msg' => "El empleado ya tiene un horario asignado en los siguientes días: $lista",
                     'icono' => 'danger',
                     'titulo' => 'Advertencia'
                 );
             } else {
                 $todoOk = true;
                 foreach ($dias as $dia) {
                     $res = $this->model->registrarHorarioEmpleado($empleado, $dia, $horario);
                     if ($res !== "ok") {
                         $todoOk = false;
                         break;
                     }
                 }
                 if ($todoOk) {
                     $msg = array('msg' => 'Horario asignado con éxito', 'icono' => 'success', 'titulo' => 'Éxito');
                 } else {
                     $msg = array('msg' => 'Error al asignar el Horario', 'icono' => 'error', 'titulo' => 'Error');
                 }
             }
         }
 
         echo json_encode($msg, JSON_UNESCAPED_UNICODE);
         die();
     }

}

?>