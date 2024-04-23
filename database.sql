-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2024 at 00:00 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `crud`
--

-- --------------------------------------------------------

--
-- Table structure for table `todos`
--

CREATE TABLE `todos` (
  `id` int(11) NOT NULL,
  `task` varchar(255) UNIQUE NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

CREATE TABLE `status`(
  `name` varchar(255) UNIQUE NOT NULL,
  `rank` int(11) NOT NULL
);

--
-- Dumping data for table `todos`
--

INSERT INTO `todos` (`id`, `task`, `status`) VALUES
(1, 'Complete assignment', 'Pending'),
(2, 'Buy groceries', 'Completed'),
(3, 'Call mom', 'Pending');

INSERT INTO `status` (`name`, `rank`) VALUES
('Completed', 4),
('Todo', 3),
('Hold', 2),
('Inprogress', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `todos`
--
ALTER TABLE `todos`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `status`
  ADD PRIMARY KEY (`name`);
--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `todos`
--
ALTER TABLE `todos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;
