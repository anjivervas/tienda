-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-06-2024 a las 22:45:23
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `test`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario`
--

CREATE TABLE `inventario` (
  `id` int(11) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `precio` decimal(20,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `inventario`
--

INSERT INTO `inventario` (`id`, `codigo`, `nombre`, `descripcion`, `precio`) VALUES
(1, '0000', 'Harina PAN', 'Harina de maiz blanco 1kg', 40),
(2, '0001', 'Harina PAN', 'Harina de maiz blanco y arroz1kg', 38),
(3, '0010', 'Harina PAN', 'Harina de maiz amarillo 1kg', 38),
(4, '0100', 'Arroz Primor', 'Arroz perlado 900g', 41),
(5, '1000', 'Arroz Primor', 'Arroz clasico 1kg', 40),
(6, '0002', 'Pasta Primor', 'Pasta corta dedales 1kg', 40),
(7, '0020', 'Pasta Primor', 'Pasta corta plumitas 1kg', 28),
(8, '0200', 'Pasta Primor', 'Pasta corta tornillo 1kg', 24),
(9, '2000', 'Pasta Primor', 'Pasta larga vermicelli 1kg', 40),
(10, '0003', 'Pasta Primor', 'Pasta linguini al huevo 1kg', 45),
(11, '0030', 'Pasta Primor', 'Pasta larga spaguetti 1kg', 39),
(12, '3000', 'Pasta Primor', 'Pasta larga vermicell 500g', 25),
(15, '0300', 'Pasta Primor', 'Pasta larga vermicell 500g', 25);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `inventario`
--
ALTER TABLE `inventario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `inventario`
--
ALTER TABLE `inventario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
