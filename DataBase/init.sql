-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-11-2020 a las 21:40:19
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `covid_19`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `casos`
--

CREATE TABLE `casos` (
  `region` varchar(50) NOT NULL,
  `casos_confirmados` int(11) NOT NULL,
  `fallecidos` int(11) NOT NULL,
  `recuperados` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `casos`
--

INSERT INTO `casos` (`region`, `casos_confirmados`, `fallecidos`, `recuperados`) VALUES
('Capital District', 335008, 7893, 304855),
('Antioquia', 183991, 3458, 169080),
('Valle del Cauca', 89703, 2961, 79898),
('Atlantico', 73447, 3146, 68863),
('Santander', 45561, 1778, 40356),
('Cundinamarca', 45007, 1272, 41325),
('Bolivar', 34055, 863, 32455),
('Cesar', 27235, 841, 24617),
('Cordoba', 27052, 1628, 24304),
('Huila', 25776, 744, 23066),
('Meta', 24566, 557, 22925),
('Norte de Santander', 23240, 1164, 20731),
('Narino', 23123, 789, 20732),
('Tolima', 22819, 700, 20227),
('Risaralda', 19238, 444, 17160),
('Magdalena', 17830, 921, 16169),
('Caldas', 17113, 332, 13871),
('Boyaca', 16708, 351, 14182),
('Sucre', 15869, 621, 14801),
('Cauca', 14036, 396, 12443),
('Quindio', 12334, 295, 10322),
('Caqueta', 11955, 414, 10661),
('La Guajira', 10660, 422, 9687),
('Casanare', 5586, 111, 4924),
('Putumayo', 4548, 207, 4096),
('Choco', 4254, 163, 3985),
('Arauca', 3604, 103, 3200),
('Amazonas', 2957, 120, 2804),
('San Andres y Providencia', 1952, 31, 1857),
('Guaviare', 1589, 25, 1484),
('Guainia', 1159, 19, 1130),
('Vaupes', 1076, 12, 1055),
('Vichada', 836, 10, 817),
('No asignados', 0, 0, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
