<aside class="left-sidebar">
      <!-- Sidebar scroll-->
      <div>
        <div class="brand-logo d-flex align-items-center justify-content-between">
          <a href="#" class="text-nowrap logo-img">
            <img src="<?= BASE_URL; ?>Assets/dist/img/logos/dark-logo.svg" width="180" alt="" />
          </a>
          <div class="close-btn d-xl-none d-block sidebartoggler cursor-pointer" id="sidebarCollapse">
            <i class="ti ti-x fs-8"></i>
          </div>
        </div>
        <!-- Sidebar navigation-->
        <nav class="sidebar-nav scroll-sidebar" data-simplebar="">
          <ul id="sidebarnav">
            <li class="nav-small-cap">
              <i class="ti ti-dots nav-small-cap-icon fs-4"></i>
              <span class="hide-menu">Home</span>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Administracion/home" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Administracion/home" aria-expanded="false">
                <span>
                  <i class="ti ti-layout-dashboard"></i>
                </span>
                <span class="hide-menu">Dashboard</span>
              </a>
            </li>
            <li class="nav-small-cap">
              <i class="ti ti-dots nav-small-cap-icon fs-4"></i>
              <span class="hide-menu">ADMINISTRACION</span>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Cargo/" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Cargo/" aria-expanded="false">
                <span>
                  <i class="ti ti-article"></i>
                </span>
                <span class="hide-menu">Cargos</span>
              </a>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Empleado/" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Empleado/" aria-expanded="false">
                <span>
                  <i class="ti ti-user-plus"></i>
                </span>
                <span class="hide-menu">Empleados</span>
              </a>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Horario/" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Horario/" aria-expanded="false">
                <span>
                  <i class="ti ti-typography"></i>
                </span>
                <span class="hide-menu">Turnos</span>
              </a>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Horario/asignar_horario" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Horario/asignar_horario" aria-expanded="false">
                <span>
                  <i class="ti ti-file-description"></i>
                </span>
                <span class="hide-menu">Asignar Turnos</span>
              </a>
            </li>
            <li class="nav-small-cap">
              <i class="ti ti-dots nav-small-cap-icon fs-4"></i>
              <span class="hide-menu">CONTROL</span>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Asistencia/" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Asistencia/" aria-expanded="false">
                <span>
                  <!-- <i class="ti ti-login"></i> -->
                  <i class="ti ti-aperture"></i>
                </span>
                <span class="hide-menu">Asistencia</span>
              </a>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link <?= $page  == "Permiso/" ? 'active' : ''; ?>" href="<?= BASE_URL ?>Permiso/" aria-expanded="false">
                <span>
                    <i class="ti ti-alert-circle"></i>
                </span>
                <span class="hide-menu">Permisos</span>
              </a>
            </li>
            <!-- <li class="nav-small-cap">
              <i class="ti ti-dots nav-small-cap-icon fs-4"></i>
              <span class="hide-menu">EXTRA</span>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link" href="./icon-tabler.html" aria-expanded="false">
                <span>
                  <i class="ti ti-mood-happy"></i>
                </span>
                <span class="hide-menu">Icons</span>
              </a>
            </li>
            <li class="sidebar-item">
              <a class="sidebar-link" href="./sample-page.html" aria-expanded="false">
                <span>
                  <i class="ti ti-aperture"></i>
                </span>
                <span class="hide-menu">Sample Page</span>
              </a>
            </li> -->
          </ul>
        </nav>
        <!-- End Sidebar navigation -->
      </div>
      <!-- End Sidebar scroll-->
    </aside>



    <!-- ESTO VA EN LA CABECERA HEADER -- MENU PARTE SUPERIOR -->
    <div class="body-wrapper">
      <!--  Header Start -->
      <header class="app-header">
        <nav class="navbar navbar-expand-lg navbar-light">
          <ul class="navbar-nav">
            <li class="nav-item d-block d-xl-none">
              <a class="nav-link sidebartoggler nav-icon-hover" id="headerCollapse" href="javascript:void(0)">
                <i class="ti ti-menu-2"></i>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link nav-icon-hover" href="javascript:void(0)">
                <i class="ti ti-bell-ringing"></i>
                <div class="notification bg-primary rounded-circle"></div>
              </a>
            </li>
          </ul>
          <div class="navbar-collapse justify-content-end px-0" id="navbarNav">
            <ul class="navbar-nav flex-row ms-auto align-items-center justify-content-end">
              <!-- <a href="https://adminmart.com/product/modernize-free-bootstrap-admin-dashboard/" target="_blank" class="btn btn-primary">Download Free</a> -->
              <li class="nav-item dropdown">
                <a class="nav-link nav-icon-hover" href="javascript:void(0)" id="drop2" data-bs-toggle="dropdown"
                  aria-expanded="false">
                  <img src="<?= BASE_URL; ?>Assets/dist/img/profile/user-1.jpg" alt="" width="35" height="35" class="rounded-circle">
                </a>
                <div class="dropdown-menu dropdown-menu-end dropdown-menu-animate-up" aria-labelledby="drop2">
                  <div class="message-body">
                    <a href="<?= BASE_URL; ?>Administracion/perfil" class="d-flex align-items-center gap-2 dropdown-item">
                      <i class="ti ti-user fs-6"></i>
                      <p class="mb-0 fs-3">Mi perfil</p>
                    </a>
                    <!-- <a href="javascript:void(0)" class="d-flex align-items-center gap-2 dropdown-item">
                      <i class="ti ti-mail fs-6"></i>
                      <p class="mb-0 fs-3">My Account</p>
                    </a>
                    <a href="javascript:void(0)" class="d-flex align-items-center gap-2 dropdown-item">
                      <i class="ti ti-list-check fs-6"></i>
                      <p class="mb-0 fs-3">My Task</p>
                    </a> -->
                    <!-- <a class="nav-link moon dark-layout" href="javascript:void(0)" style="display: flex;">
                      <i class="ti ti-moon moon" style="display: flex;"></i>
                    </a> -->
                    <a href="<?= BASE_URL ?>Usuario/salir" class="btn btn-outline-primary mx-3 mt-2 d-block">Salir</a>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </nav>
      </header>