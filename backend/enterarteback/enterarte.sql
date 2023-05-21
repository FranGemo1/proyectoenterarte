-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 03, 2023 at 05:03 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `enterarte`
--

-- --------------------------------------------------------

--
-- Table structure for table `eventos`
--

CREATE TABLE `eventos` (
  `idEvento` int(11) NOT NULL,
  `idUser` int(11) DEFAULT NULL,
  `idTicket` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `eventosdata`
--

CREATE TABLE `eventosdata` (
  `idEventoData` int(11) NOT NULL,
  `idEvento` int(11) DEFAULT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `foto` blob DEFAULT NULL,
  `categoria` varchar(20) DEFAULT NULL,
  `genero` varchar(20) DEFAULT NULL,
  `provincia` varchar(20) DEFAULT NULL,
  `localidad` varchar(20) DEFAULT NULL,
  `calle` varchar(30) DEFAULT NULL,
  `numero` varchar(10) DEFAULT NULL,
  `rss` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `permisos`
--

CREATE TABLE `permisos` (
  `idPermiso` int(11) NOT NULL,
  `idUser` int(11) DEFAULT NULL,
  `restricciones` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `idRol` int(11) NOT NULL,
  `idUser` int(11) DEFAULT NULL,
  `rol` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `idTicket` int(11) NOT NULL,
  `idEvento` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `fechayhora` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `idUserData` int(11) NOT NULL,
  `idUser` int(11) NOT NULL,
  `nombres` varchar(40) COLLATE utf8mb4_spanish_ci NOT NULL,
  `apellido` varchar(40) COLLATE utf8mb4_spanish_ci NOT NULL,
  `fechaNac` date NOT NULL,
  `tel` varchar(15) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `idUser` int(11) NOT NULL,
  `idUserData` int(11) DEFAULT NULL,
  `idPermiso` int(11) DEFAULT NULL,
  `idRol` int(11) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `eventos`
--
ALTER TABLE `eventos`
  ADD PRIMARY KEY (`idEvento`),
  ADD KEY `eventos` (`idUser`),
  ADD KEY `idTicketFk` (`idTicket`);

--
-- Indexes for table `eventosdata`
--
ALTER TABLE `eventosdata`
  ADD PRIMARY KEY (`idEventoData`),
  ADD KEY `idEventoFk` (`idEvento`);

--
-- Indexes for table `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`idPermiso`),
  ADD KEY `idUser` (`idUser`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`idRol`),
  ADD KEY `roles` (`idUser`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
  ADD PRIMARY KEY (`idTicket`),
  ADD KEY `ticket` (`idEvento`);

--
-- Indexes for table `userdata`
--
ALTER TABLE `userdata`
  ADD PRIMARY KEY (`idUserData`),
  ADD KEY `idUserFk` (`idUser`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`idUser`),
  ADD KEY `idUserDataFk` (`idUserData`),
  ADD KEY `idPermisoFk` (`idPermiso`),
  ADD KEY `idRolFk` (`idRol`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `eventos`
--
ALTER TABLE `eventos`
  ADD CONSTRAINT `eventos` FOREIGN KEY (`idUser`) REFERENCES `users` (`idUser`),
  ADD CONSTRAINT `idTicketFk` FOREIGN KEY (`idTicket`) REFERENCES `ticket` (`idTicket`);

--
-- Constraints for table `eventosdata`
--
ALTER TABLE `eventosdata`
  ADD CONSTRAINT `idEventoFk` FOREIGN KEY (`idEvento`) REFERENCES `eventos` (`idEvento`);

--
-- Constraints for table `permisos`
--
ALTER TABLE `permisos`
  ADD CONSTRAINT `permisos_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`idUser`);

--
-- Constraints for table `roles`
--
ALTER TABLE `roles`
  ADD CONSTRAINT `roles` FOREIGN KEY (`idUser`) REFERENCES `users` (`idUser`);

--
-- Constraints for table `ticket`
--
ALTER TABLE `ticket`
  ADD CONSTRAINT `ticket` FOREIGN KEY (`idEvento`) REFERENCES `eventos` (`idEvento`);

--
-- Constraints for table `userdata`
--
ALTER TABLE `userdata`
  ADD CONSTRAINT `idUserFk` FOREIGN KEY (`idUser`) REFERENCES `users` (`idUser`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `idPermisoFk` FOREIGN KEY (`idPermiso`) REFERENCES `permisos` (`idPermiso`),
  ADD CONSTRAINT `idRolFk` FOREIGN KEY (`idRol`) REFERENCES `roles` (`idRol`),
  ADD CONSTRAINT `idUserDataFk` FOREIGN KEY (`idUserData`) REFERENCES `userdata` (`idUserData`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
