<?php

class Empleado extends Controller
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
            $data['cargos'] = $this->model->getCargo();
            $this->views->getView($this, "index", $data);

        } else {
            header("Location: " . BASE_URL);
        }
    }

    public function ver_empleado($id)
    {
        $id_usuario = $_SESSION['id_usuario'];
        if ($id_usuario) {
            $data['empleado'] = $this->model->getEmpleado($id);
            $this->views->getView($this, "ver_empleado", $data);

        } else {
            header("Location: " . BASE_URL);
        }
    }

    public function listar_empleados()
    {
        $data = $this->model->getEmpleados();
        for ($i = 0; $i < count($data); $i++) {
            if ($data[$i]['estado'] == 'activo') {
                $data[$i]['estado'] = '<span class="badge bg-success rounded-3 fw-semibold">Activo</span>';
            } else {
                $data[$i]['estado'] = '<span class="badge bg-danger rounded-3 fw-semibold">Inactivo</span>';
            }

            $data[$i]['acciones'] = '
                <button class="btn btn-primary btn-action" onclick="btnEditarEmpleado(' . $data[$i]['id'] . ')" title="Editar">
                    <i class="ti ti-pencil"></i>
                </button>

                <a class="btn btn-info btn-action" title="Ver" href="'. BASE_URL.'Empleado/ver_empleado/'.$data[$i]['id'].'" "><i class="ti ti-eye"></i></a>

                <button class="btn btn-danger btn-action" onclick="btnEliminarEmpleado(' . $data[$i]['id'] . ')" title="Eliminar">
                    <i class="ti ti-trash"></i>
                </button>
            ';
        }

        // Devolver JSON limpio
        header('Content-Type: application/json');
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        exit;
    }

    public function modificarEmpleado()
    {
        $id = $_POST['id'];
        $nombre = $_POST['nombre'];
        $apellido = $_POST['apellido'];
        $dni = $_POST['dni'];
        $telefono = $_POST['telefono'];
        $genero = $_POST['genero'];
        $fecha_nacimiento = $_POST['fecha_nacimiento'];
        $direccion = $_POST['direccion'];
        $email = $_POST['email'];
        $cargos = $_POST['cargos'];
        $estado = $_POST['estado'];

        // Si no se envía un ID, procede a realizar el registro
        if (!$id == "") {
            if (empty($nombre) || empty($apellido) || empty($dni) || empty($telefono) || empty($genero)
                || empty($fecha_nacimiento) || empty($direccion) || empty($email) || empty($cargos) || empty($estado)) 
            {
                $msg = "Todos los campos son obligatorios";
                
            } else {
                $data = $this->model->putModificarEmpleado($nombre, $apellido, $dni, $telefono, $genero, $fecha_nacimiento, $direccion, $email, $cargos, $estado, $id);
                if ($data == "modificado") {
                    $msg = array('msg' => 'Empleado Modificado Correcamente', 'icono' => 'success', 'titulo' => 'Exito');
                } else {
                    $msg = array('msg' => 'Error al modificar el Empleado', 'icono' => 'error', 'titulo' => 'Error');
                }
            }
        }

        header('Content-Type: application/json'); // 👈 fuerza a devolver JSON
        echo json_encode($msg, JSON_UNESCAPED_UNICODE);
        exit;
    }

    public function editar($id)
    {
        $data = $this->model->editarEmpleado($id);
        header('Content-Type: application/json'); // 👈 fuerza a devolver JSON
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        exit;
    }

    public function eliminar($id)
    {
        $data = $this->model->eliminarEmpleado($id);
        if ($data == 1) {
            $msg = array('msg' => 'Empleado elimiado exitosamente', 'icono' => 'success', 'titulo' => 'Exito');
        } else {
            $msg = array('msg' => 'Error al eliminar el Empleado', 'icono' => 'error', 'titulo' => 'Error');
        }
        header('Content-Type: application/json'); // 👈 fuerza a devolver JSON
        echo json_encode($data, JSON_UNESCAPED_UNICODE);
        exit;
    }
}
