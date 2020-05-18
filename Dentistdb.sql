-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: dentistdb
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `medication_catalog`
--

DROP TABLE IF EXISTS `medication_catalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medication_catalog` (
  `id_medication` int NOT NULL AUTO_INCREMENT,
  `medication_name` varchar(45) NOT NULL,
  `indregients` varchar(45) NOT NULL,
  PRIMARY KEY (`id_medication`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medication_catalog`
--

LOCK TABLES `medication_catalog` WRITE;
/*!40000 ALTER TABLE `medication_catalog` DISABLE KEYS */;
/*!40000 ALTER TABLE `medication_catalog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `tckn` varchar(15) NOT NULL,
  `patientname` varchar(45) NOT NULL,
  `patientsurname` varchar(45) NOT NULL,
  `dob` varchar(10) NOT NULL,
  `phone` varchar(45) NOT NULL,
  PRIMARY KEY (`tckn`),
  UNIQUE KEY `tckn_UNIQUE` (`tckn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_history`
--

DROP TABLE IF EXISTS `patient_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_history` (
  `index` int NOT NULL AUTO_INCREMENT,
  `pt_tckn` varchar(45) NOT NULL,
  `ptreatment_id` int NOT NULL,
  PRIMARY KEY (`index`),
  KEY `pt_tckn_idx` (`pt_tckn`),
  KEY `ptreatment_id` (`ptreatment_id`),
  CONSTRAINT `pat_tckn` FOREIGN KEY (`pt_tckn`) REFERENCES `patient` (`tckn`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `patient_history_ibfk_1` FOREIGN KEY (`ptreatment_id`) REFERENCES `treatment` (`id_treatment`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_history`
--

LOCK TABLES `patient_history` WRITE;
/*!40000 ALTER TABLE `patient_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `problem_catalog`
--

DROP TABLE IF EXISTS `problem_catalog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `problem_catalog` (
  `id_problem` int NOT NULL AUTO_INCREMENT,
  `problem_name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_problem`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `problem_catalog`
--

LOCK TABLES `problem_catalog` WRITE;
/*!40000 ALTER TABLE `problem_catalog` DISABLE KEYS */;
/*!40000 ALTER TABLE `problem_catalog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatment`
--

DROP TABLE IF EXISTS `treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treatment` (
  `id_treatment` int NOT NULL AUTO_INCREMENT,
  `patient_tckn` varchar(45) NOT NULL,
  `medication_id` int NOT NULL,
  `problem_id` int NOT NULL,
  PRIMARY KEY (`id_treatment`),
  KEY `patient_tckn_idx` (`patient_tckn`),
  KEY `medication_id` (`medication_id`),
  KEY `problem_id` (`problem_id`),
  CONSTRAINT `patient_tckn` FOREIGN KEY (`patient_tckn`) REFERENCES `patient` (`tckn`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `treatment_ibfk_1` FOREIGN KEY (`medication_id`) REFERENCES `medication_catalog` (`id_medication`),
  CONSTRAINT `treatment_ibfk_2` FOREIGN KEY (`problem_id`) REFERENCES `problem_catalog` (`id_problem`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatment`
--

LOCK TABLES `treatment` WRITE;
/*!40000 ALTER TABLE `treatment` DISABLE KEYS */;
/*!40000 ALTER TABLE `treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_account`
--

DROP TABLE IF EXISTS `user_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_account` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `user_surname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `mobile` varchar(45) NOT NULL,
  `is_active` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_account`
--

LOCK TABLES `user_account` WRITE;
/*!40000 ALTER TABLE `user_account` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit`
--

DROP TABLE IF EXISTS `visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit` (
  `id_visit` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `patient_tckn` varchar(45) NOT NULL,
  PRIMARY KEY (`id_visit`),
  KEY `user_id` (`user_id`),
  KEY `patient_tckn` (`patient_tckn`),
  CONSTRAINT `visit_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_account` (`id`),
  CONSTRAINT `visit_ibfk_2` FOREIGN KEY (`patient_tckn`) REFERENCES `patient` (`tckn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit`
--

LOCK TABLES `visit` WRITE;
/*!40000 ALTER TABLE `visit` DISABLE KEYS */;
/*!40000 ALTER TABLE `visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'dentistdb'
--

--
-- Dumping routines for database 'dentistdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-18 13:33:02
