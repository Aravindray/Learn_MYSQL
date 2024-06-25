-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: cookbook
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mail`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `t` datetime DEFAULT NULL,
  `srcuser` varchar(8) DEFAULT NULL,
  `srchost` varchar(20) DEFAULT NULL,
  `dstuser` varchar(8) DEFAULT NULL,
  `dsthost` varchar(20) DEFAULT NULL,
  `size` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `t` (`t`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mail`
--

LOCK TABLES `mail` WRITE;
/*!40000 ALTER TABLE `mail` DISABLE KEYS */;
INSERT INTO `mail` VALUES (1,'2014-05-11 10:15:08','barb','saturn','tricia','mars',58274),(2,'2014-05-12 12:48:13','tricia','mars','gene','venus',194925),(3,'2014-05-12 15:02:49','phil','mars','phil','saturn',1048),(4,'2014-05-12 18:59:18','barb','saturn','tricia','venus',271),(5,'2014-05-14 09:31:37','gene','venus','barb','mars',2291),(6,'2014-05-14 11:52:17','phil','mars','tricia','saturn',5781),(7,'2014-05-14 14:42:21','barb','venus','barb','venus',98151),(8,'2014-05-14 17:03:01','tricia','saturn','phil','venus',2394482),(9,'2014-05-15 07:17:48','gene','mars','gene','saturn',3824),(10,'2014-05-15 08:50:57','phil','venus','phil','venus',978),(11,'2014-05-15 10:25:52','gene','mars','tricia','saturn',998532),(12,'2014-05-15 17:35:31','gene','saturn','gene','mars',3856),(13,'2014-05-16 09:00:28','gene','venus','barb','mars',613),(14,'2014-05-16 23:04:19','phil','venus','barb','venus',10294),(15,'2014-05-19 12:49:23','phil','mars','tricia','saturn',873),(16,'2014-05-19 22:21:51','gene','saturn','gene','venus',23992);
/*!40000 ALTER TABLE `mail` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-25 16:27:30
