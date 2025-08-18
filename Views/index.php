<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Modernize Free</title>
  <link rel="shortcut icon" type="image/png" href="<?= BASE_URL; ?>Assets/dist/img/logos/favicon.png" />
  <link rel="stylesheet" href="<?= BASE_URL; ?>Assets/dist/css/styles.min.css" />
</head>

<body>
  <!--  Body Wrapper -->
  <div class="page-wrapper" id="main-wrapper" data-layout="vertical" data-navbarbg="skin6" data-sidebartype="full"
    data-sidebar-position="fixed" data-header-position="fixed">
    <div
      class="position-relative overflow-hidden radial-gradient min-vh-100 d-flex align-items-center justify-content-center">
      <div class="d-flex align-items-center justify-content-center w-100">
        <div class="row justify-content-center w-100">
          <div class="col-md-8 col-lg-6 col-xxl-3">
            <div class="card mb-0">
              <div class="card-body">
                <a href="./index.html" class="text-nowrap logo-img text-center d-block py-3 w-100">
                  <img src="<?= BASE_URL; ?>Assets/dist/img/logos/dark-logo.svg" width="180" alt="">
                </a>
                <p class="text-center">Control de Asitencia Satipo</p>
                <form id="frmLogin">
                  <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Usuario</label>
                    <input type="text" name="usuario" id="usuario" class="form-control" placeholder="admin123" >
                  </div>
                  <div class="mb-4">
                    <label for="exampleInputPassword1" class="form-label">Contraseña</label>
                    <input type="password" name="password" id="password" class="form-control" placeholder="**********" >
                  </div>
                  <div class="d-flex align-items-center justify-content-between mb-4">
                    <div class="form-check">
                      <input class="form-check-input primary" type="checkbox" value="" id="flexCheckChecked" checked>
                      <label class="form-check-label text-dark" for="flexCheckChecked">
                        Olvidaste la contraseña ?
                      </label>
                    </div>
                    <!-- <a class="text-primary fw-bold" href="./index.html">Forgot Password ?</a> -->
                  </div>
                  <button  type="submit" onclick="frmLogin(event);" class="btn btn-primary w-100 py-8 fs-4 mb-4 rounded-2">Iniciar</button>
                  <div class="d-flex align-items-center justify-content-center">
                    <p class="fs-4 mb-0 fw-bold">IMPRENTAS SATIPO</p>
                    <!-- <a class="text-primary fw-bold ms-2" href="./authentication-register.html">Create an account</a> -->
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <script src="<?= BASE_URL; ?>Assets/js/sweetalert2.all.min.js"></script>
  <script src="<?= BASE_URL; ?>Assets/dist/libs/jquery/dist/jquery.min.js"></script>
  <script src="<?= BASE_URL; ?>Assets/dist/libs/bootstrap/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    const BASE_URL = "<?php echo BASE_URL; ?>";
  </script>
  <script src="<?= BASE_URL; ?>Assets/js/login.js"></script>
</body>

</html>