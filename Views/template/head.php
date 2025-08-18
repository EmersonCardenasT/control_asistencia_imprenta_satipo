<?php

$directorio = $_SERVER['REQUEST_URI'];
$path = parse_url($directorio, PHP_URL_PATH);
$componentes = explode('/', $path);
// Capturamos el tercer y cuarto segmento de la URL y los concatenamos
// Se puede concatenar mas tambien.
$page = isset($componentes[3]) ? $componentes[3] : '';
$page .= isset($componentes[4]) ? '/' . $componentes[4] : '';

?>

<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Imprenta Satipo EIRL</title>
  <link rel="shortcut icon" type="image/png" href="<?= BASE_URL; ?>Assets/dist/img/logos/favicon.png" />
  <link rel="stylesheet" href="<?= BASE_URL; ?>Assets/dist/css/styles.min.css" />

  <!-- jQuery -->
  <script src="<?= BASE_URL ?>Assets/dist/js/jquery-3.6.0.min.js"></script>

  <!-- DataTables CSS + JS -->
  <link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/dataTables.bootstrap5.min.css" />
  <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.datatables.net/1.13.4/js/dataTables.bootstrap5.min.js"></script>

  <!-- SweetAlert2 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css" rel="stylesheet">

  <!-- SweetAlert2 JS -->
  <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>


  <!-- Tu archivo JS -->
  <script>
    const BASE_URL = "<?= BASE_URL; ?>";
  </script>
  <script src="<?= BASE_URL; ?>Assets/js/funciones.js"></script>

  <style>
    .btn-action {
      padding: 0.5rem 0.7rem;
      font-size: 0.95rem;
      line-height: 1;
      margin-left: 2.5px;
      /* mantiene compacto */
    }

    .btn-action i {
      font-size: 1rem;
      /* controla el tamaño del ícono */
    }

    .badge {
      font-size: 0.7rem;
      /* controla el tamaño del badge */
    }
  </style>

</head>

<body>
  <!--  Body Wrapper -->
  <div class="page-wrapper" id="main-wrapper" data-layout="vertical" data-navbarbg="skin6" data-sidebartype="full"
    data-sidebar-position="fixed" data-header-position="fixed">