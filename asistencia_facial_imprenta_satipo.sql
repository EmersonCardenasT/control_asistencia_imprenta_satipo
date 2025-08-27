-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-08-2025 a las 19:18:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `asistencia_facial_imprenta_satipo`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencia`
--

CREATE TABLE `asistencia` (
  `id` int(11) NOT NULL,
  `empleado_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora_entrada` time DEFAULT NULL,
  `hora_salida` time DEFAULT NULL,
  `estado` enum('presente','falta','permiso','tarde') DEFAULT 'presente',
  `bloque` varchar(50) DEFAULT NULL,
  `minutos_tarde` int(11) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE `cargos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `estado` enum('activo','inactivo') DEFAULT 'activo',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`id`, `nombre`, `estado`, `created_at`, `updated_at`) VALUES
(1, 'Administrador', 'activo', '2025-08-18 13:16:51', '2025-08-18 13:16:51'),
(2, 'Empleado', 'activo', '2025-08-18 13:16:51', '2025-08-18 13:16:51'),
(3, 'Cargo 1', 'activo', '2025-08-18 14:58:56', '2025-08-18 14:58:56'),
(4, 'Cargo 2', 'activo', '2025-08-18 14:58:56', '2025-08-18 14:58:56'),
(5, 'Cargo 355555', 'activo', '2025-08-18 14:59:27', '2025-08-18 15:55:51'),
(7, 'Cargo 5', 'activo', '2025-08-18 14:59:27', '2025-08-18 14:59:27'),
(9, 'Cargo 7', 'activo', '2025-08-18 14:59:27', '2025-08-18 14:59:27'),
(12, 'Cargo 10', 'activo', '2025-08-18 14:59:27', '2025-08-18 14:59:27'),
(14, 'Cargo 12', 'activo', '2025-08-18 14:59:27', '2025-08-18 14:59:27'),
(15, 'Cargo representativos s', 'activo', '2025-08-18 15:56:54', '2025-08-18 18:06:31'),
(16, 'Encargado de planta 2ss', 'activo', '2025-08-18 15:59:33', '2025-08-18 16:08:14'),
(18, ' gasdg asdg as', 'activo', '2025-08-18 18:06:56', '2025-08-18 18:06:56');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` int(11) NOT NULL,
  `foto` varchar(255) DEFAULT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `dni` varchar(20) NOT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `genero` enum('M','F','O') DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cargo_id` int(11) DEFAULT NULL,
  `estado` enum('activo','inactivo') DEFAULT 'activo',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `foto`, `nombre`, `apellido`, `dni`, `telefono`, `genero`, `fecha_nacimiento`, `direccion`, `email`, `cargo_id`, `estado`, `created_at`, `updated_at`) VALUES
(2, NULL, 'Emer', 'Cardenas', '87044122', '929450111', 'M', '2001-05-01', 'san pfpfpf', 'afsd@gmail.com', 15, 'activo', '2025-08-18 17:12:50', '2025-08-18 17:12:50'),
(4, NULL, 'Carlos', 'Gutiérrez', '76543210', '945123456', 'M', '1995-02-10', 'Jr. Los Pinos 456', 'carlos.gutierrez@gmail.com', 14, 'activo', '2025-08-18 17:13:17', '2025-08-18 18:07:11'),
(5, NULL, 'María', 'López', '\n00224411', '987112233', 'F', '2000-12-25', 'Calle Las Flores 789', 'maria.lopez@gmail.com', 15, 'inactivo', '2025-08-18 17:13:17', '2025-08-21 06:25:48'),
(7, NULL, 'Ana s1', 'Torres S S', '80112233', '934556677', 'F', '1999-11-19', 'Urb. Santa Clara Mz A Lt 5', 'ana.torres@gmail.com', 12, 'inactivo', '2025-08-18 17:13:17', '2025-08-19 16:10:19'),
(31, NULL, 'Lucía', 'Morales', '76678901', '932109876', 'F', '1999-12-30', 'Av. Central 900', 'lucia.morales@gmail.com', 14, 'inactivo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(32, NULL, 'Diego', 'Castro', '76789012', '921098765', 'M', '1994-06-18', 'Jr. San Juan 100', 'diego.castro@gmail.com', 15, 'activo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(33, NULL, 'Gabriela', 'Herrera', '76890123', '910987654', 'F', '1997-08-27', 'Calle Los Rosales 45', 'gabriela.herrera@gmail.com', 9, 'activo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(34, NULL, 'Ricardo', 'Vargas', '76901234', '989876543', 'M', '1989-02-12', 'Av. Las Torres 12', 'ricardo.vargas@gmail.com', 14, 'inactivo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(35, NULL, 'Valeria', 'Silva', '76112345', '978765432', 'F', '1995-04-05', 'Urb. La Molina C-23', 'valeria.silva@gmail.com', 15, 'activo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(36, NULL, 'Fernando', 'Chávez', '76223456', '967654321', 'M', '1991-11-29', 'Jr. Los Cedros 78', 'fernando.chavez@gmail.com', 14, 'activo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(37, NULL, 'Carolina', 'Peña', '76334567', '956543210', 'F', '2000-10-10', 'Av. Universitaria 555', 'carolina.pena@gmail.com', 15, 'inactivo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(38, NULL, 'Hugo', 'Salazar', '76445678', '945432109', 'M', '1992-09-15', 'Calle Las Gardenias 76', 'hugo.salazar@gmail.com', 14, 'activo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(39, NULL, 'Natalia', 'Ríos', '76556789', '934321098', 'F', '1998-03-25', 'Jr. Los Sauces 34', 'natalia.rios@gmail.com', 14, 'activo', '2025-08-21 04:18:52', '2025-08-21 04:18:52'),
(40, NULL, 'Álvaro', 'Mendoza', '76667890', '923210987', 'M', '1997-12-08', 'Urb. San Luis G-12', 'alvaro.mendoza@gmail.com', 15, 'inactivo', '2025-08-21 04:18:52', '2025-08-21 04:18:52');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado_contrato`
--

CREATE TABLE `empleado_contrato` (
  `id` int(11) NOT NULL,
  `empleado_id` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date DEFAULT NULL,
  `estado` enum('activo','finalizado') DEFAULT 'activo',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado_contrato`
--

INSERT INTO `empleado_contrato` (`id`, `empleado_id`, `fecha_inicio`, `fecha_fin`, `estado`, `created_at`, `updated_at`) VALUES
(1, 2, '2025-08-21', '2026-08-27', 'activo', '2025-08-21 14:33:20', '2025-08-21 14:33:20'),
(2, 4, '2025-08-21', '2026-08-29', 'activo', '2025-08-21 14:35:14', '2025-08-21 14:35:14'),
(3, 5, '2025-08-21', '2025-12-31', 'activo', '2025-08-21 14:35:14', '2025-08-21 14:35:14'),
(10, 31, '2025-08-21', '2026-06-29', 'activo', '2025-08-21 14:37:20', '2025-08-21 14:37:20'),
(11, 32, '2025-08-21', '2026-07-14', 'activo', '2025-08-21 14:37:20', '2025-08-21 14:37:20'),
(12, 33, '2025-08-21', '0000-00-00', 'activo', '2025-08-21 14:37:20', '2025-08-21 14:37:20'),
(13, 34, '2025-08-21', '2026-05-31', 'activo', '2025-08-21 14:37:20', '2025-08-21 14:37:20'),
(14, 35, '2025-08-21', '2026-11-15', 'activo', '2025-08-21 14:37:20', '2025-08-21 14:37:20'),
(15, 36, '2025-08-21', '2026-12-31', 'activo', '2025-08-21 14:37:20', '2025-08-21 14:37:20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id` int(11) NOT NULL,
  `empleado_id` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_fin` date NOT NULL,
  `tipo_permiso` enum('vacaciones','medico','personal','otro') NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `estado` enum('pendiente','aprobado','rechazado') DEFAULT 'pendiente',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos`
--

CREATE TABLE `turnos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `hora_entrada` time NOT NULL,
  `hora_salida` time NOT NULL,
  `estado` enum('activo','inactivo') DEFAULT 'activo',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `turnos`
--

INSERT INTO `turnos` (`id`, `nombre`, `hora_entrada`, `hora_salida`, `estado`, `created_at`, `updated_at`) VALUES
(1, 'Turno Temprano', '08:00:00', '13:00:00', 'activo', '2025-08-19 16:53:45', '2025-08-19 16:53:45'),
(3, 'Turno Tarde', '13:30:00', '18:30:00', 'activo', '2025-08-19 17:04:24', '2025-08-19 17:04:24'),
(4, 'Turno Noche', '19:00:00', '23:00:00', 'activo', '2025-08-19 17:04:35', '2025-08-19 17:04:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `turnos_empleado`
--

CREATE TABLE `turnos_empleado` (
  `id` int(11) NOT NULL,
  `empleado_id` int(11) NOT NULL,
  `dia_semana` tinyint(4) NOT NULL COMMENT '0=Domingo, 1=Lunes, ... 6=Sabado',
  `turno_id` int(11) NOT NULL,
  `bloque` varchar(50) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `turnos_empleado`
--

INSERT INTO `turnos_empleado` (`id`, `empleado_id`, `dia_semana`, `turno_id`, `bloque`, `created_at`, `updated_at`) VALUES
(1, 2, 1, 1, NULL, '2025-08-21 06:15:37', '2025-08-21 06:15:37'),
(4, 2, 2, 1, NULL, '2025-08-21 06:16:47', '2025-08-21 06:16:47'),
(5, 2, 3, 3, NULL, '2025-08-21 06:16:47', '2025-08-21 06:16:47'),
(6, 2, 4, 3, NULL, '2025-08-21 06:16:47', '2025-08-21 06:16:47'),
(7, 4, 0, 1, NULL, '2025-08-21 06:22:20', '2025-08-21 06:22:20'),
(8, 4, 1, 1, NULL, '2025-08-21 06:22:20', '2025-08-21 06:22:20'),
(9, 4, 2, 1, NULL, '2025-08-21 06:22:20', '2025-08-21 06:22:20'),
(10, 31, 3, 3, NULL, '2025-08-21 06:26:00', '2025-08-21 06:26:00'),
(11, 31, 4, 3, NULL, '2025-08-21 06:26:00', '2025-08-21 06:26:00'),
(12, 31, 5, 3, NULL, '2025-08-21 06:26:00', '2025-08-21 06:26:00'),
(13, 31, 2, 4, NULL, '2025-08-21 06:26:29', '2025-08-21 06:26:29'),
(14, 39, 0, 1, NULL, '2025-08-21 06:28:56', '2025-08-21 06:28:56'),
(15, 39, 2, 1, NULL, '2025-08-21 06:28:56', '2025-08-21 06:28:56'),
(16, 39, 1, 3, NULL, '2025-08-21 06:29:14', '2025-08-21 06:29:14'),
(17, 40, 6, 4, NULL, '2025-08-21 06:30:43', '2025-08-21 06:30:43'),
(18, 38, 1, 3, NULL, '2025-08-21 06:35:20', '2025-08-21 06:35:20'),
(19, 37, 0, 4, NULL, '2025-08-21 06:35:39', '2025-08-21 06:35:39'),
(20, 37, 2, 4, NULL, '2025-08-21 06:35:39', '2025-08-21 06:35:39'),
(21, 37, 4, 4, NULL, '2025-08-21 06:35:39', '2025-08-21 06:35:39'),
(22, 37, 1, 1, NULL, '2025-08-21 06:35:52', '2025-08-21 06:35:52'),
(23, 37, 3, 1, NULL, '2025-08-21 06:35:52', '2025-08-21 06:35:52');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `dni` int(11) NOT NULL,
  `usuario` varchar(255) NOT NULL,
  `password` varchar(30) NOT NULL,
  `estado` tinyint(4) NOT NULL DEFAULT 1,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `dni`, `usuario`, `password`, `estado`, `created_at`) VALUES
(1, 'Emerson', 'Cardenas', 76015187, 'admin', 'admin', 1, '2025-08-17 04:07:22');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_asistencia_empleado` (`empleado_id`);

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `dni` (`dni`),
  ADD UNIQUE KEY `email` (`email`),
  ADD KEY `fk_empleado_cargo` (`cargo_id`);

--
-- Indices de la tabla `empleado_contrato`
--
ALTER TABLE `empleado_contrato`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_contrato_empleado` (`empleado_id`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_permiso_empleado` (`empleado_id`);

--
-- Indices de la tabla `turnos`
--
ALTER TABLE `turnos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `turnos_empleado`
--
ALTER TABLE `turnos_empleado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_turno_empleado` (`empleado_id`),
  ADD KEY `fk_turno` (`turno_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `empleado_contrato`
--
ALTER TABLE `empleado_contrato`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `turnos`
--
ALTER TABLE `turnos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `turnos_empleado`
--
ALTER TABLE `turnos_empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencia`
--
ALTER TABLE `asistencia`
  ADD CONSTRAINT `fk_asistencia_empleado` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`);

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `fk_empleado_cargo` FOREIGN KEY (`cargo_id`) REFERENCES `cargos` (`id`);

--
-- Filtros para la tabla `empleado_contrato`
--
ALTER TABLE `empleado_contrato`
  ADD CONSTRAINT `fk_contrato_empleado` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`);

--
-- Filtros para la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD CONSTRAINT `fk_permiso_empleado` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`);

--
-- Filtros para la tabla `turnos_empleado`
--
ALTER TABLE `turnos_empleado`
  ADD CONSTRAINT `fk_turno` FOREIGN KEY (`turno_id`) REFERENCES `turnos` (`id`),
  ADD CONSTRAINT `fk_turno_empleado` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
