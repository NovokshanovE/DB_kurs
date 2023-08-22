-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: restaurant
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `external_user`
--

DROP TABLE IF EXISTS `external_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `external_user` (
  `user_id` int NOT NULL,
  `user_group` varchar(45) DEFAULT NULL,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `external_user`
--

LOCK TABLES `external_user` WRITE;
/*!40000 ALTER TABLE `external_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `external_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `internal_user`
--

DROP TABLE IF EXISTS `internal_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `internal_user` (
  `user_id` int NOT NULL,
  `user_group` varchar(45) DEFAULT NULL,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internal_user`
--

LOCK TABLES `internal_user` WRITE;
/*!40000 ALTER TABLE `internal_user` DISABLE KEYS */;
INSERT INTO `internal_user` VALUES (1,'maneger','work','12345'),(2,'admin','adm','root'),(3,'waiter','waiter1','in_1holl'),(4,'waiter','waiter2','in_holl2');
/*!40000 ALTER TABLE `internal_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menu`
--

DROP TABLE IF EXISTS `menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menu` (
  `id_M` int NOT NULL,
  `name_dishes` varchar(45) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id_M`),
  UNIQUE KEY `name_dishes_UNIQUE` (`name_dishes`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menu`
--

LOCK TABLES `menu` WRITE;
/*!40000 ALTER TABLE `menu` DISABLE KEYS */;
INSERT INTO `menu` VALUES (1,'Грибной Крем-суп',500),(2,'Макороны по флоцки',450),(3,'Мясная лазанья',480),(4,'Наполеон',400),(5,'Фондан с ванильным мороженым',600),(6,'Глинтвейн',500);
/*!40000 ALTER TABLE `menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_lines`
--

DROP TABLE IF EXISTS `order_lines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_lines` (
  `id_OL` int NOT NULL AUTO_INCREMENT,
  `Menu_id_M` int DEFAULT NULL,
  `Ordering_id_O` int DEFAULT NULL,
  `dishes_amount` int DEFAULT '1',
  PRIMARY KEY (`id_OL`),
  KEY `Menu_id_M_idx` (`Menu_id_M`),
  KEY `FK_id_O_idx` (`Ordering_id_O`),
  CONSTRAINT `Menu_id_M` FOREIGN KEY (`Menu_id_M`) REFERENCES `menu` (`id_M`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_lines`
--

LOCK TABLES `order_lines` WRITE;
/*!40000 ALTER TABLE `order_lines` DISABLE KEYS */;
INSERT INTO `order_lines` VALUES (1,1,1,1),(2,1,1,1),(3,3,3,1),(4,2,4,1),(5,4,3,1),(6,1,3,1),(7,6,1,1),(8,6,4,1),(9,6,4,1),(10,4,6,1),(11,4,6,1),(12,4,6,0),(13,4,6,20),(14,4,6,2),(15,1,1,0),(16,6,11,2),(17,5,11,4),(18,4,12,5),(19,6,12,7),(20,4,13,8),(21,2,13,3),(23,1,15,4),(24,2,15,1),(25,3,15,2),(26,4,15,1),(27,1,16,2),(28,3,16,1),(29,1,18,1),(30,1,19,1),(31,2,19,1),(32,1,20,1),(33,3,20,1),(34,4,20,1),(35,1,23,3),(36,2,23,2),(37,3,23,1),(38,4,23,1),(39,1,26,1),(40,4,26,1),(41,5,26,1),(42,1,27,1),(43,2,27,1),(44,4,27,1),(45,1,28,2),(46,2,28,1),(47,3,28,1),(48,1,33,2),(49,2,33,3),(50,1,34,1),(51,2,34,1),(52,1,35,1),(53,3,35,1),(54,1,36,1),(55,5,36,1),(56,6,36,1),(57,1,45,2),(58,2,45,1),(59,3,45,1),(60,1,50,2),(61,4,50,1),(62,5,50,1),(63,1,51,1),(64,3,51,1),(65,2,52,2),(66,3,52,1),(67,4,52,1),(68,1,53,1),(69,2,53,1);
/*!40000 ALTER TABLE `order_lines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordering`
--

DROP TABLE IF EXISTS `ordering`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordering` (
  `id_O` int NOT NULL AUTO_INCREMENT,
  `order_date` date DEFAULT NULL,
  `Table_id_T` int DEFAULT NULL,
  `Waiter_id_W` int DEFAULT NULL,
  PRIMARY KEY (`id_O`),
  KEY `Table_id_T_idx` (`Table_id_T`),
  KEY `Waiter_id_W_idx` (`Waiter_id_W`),
  CONSTRAINT `FK_id_T` FOREIGN KEY (`Table_id_T`) REFERENCES `table` (`id_T`),
  CONSTRAINT `FK_id_W` FOREIGN KEY (`Waiter_id_W`) REFERENCES `waiter` (`id_W`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordering`
--

LOCK TABLES `ordering` WRITE;
/*!40000 ALTER TABLE `ordering` DISABLE KEYS */;
INSERT INTO `ordering` VALUES (15,'2022-11-30',1,1),(16,'2022-11-30',1,1),(17,'2022-12-04',1,1),(18,'2022-12-04',1,1),(19,'2022-12-04',1,1),(20,'2022-12-04',3,1),(21,'2022-12-04',3,1),(22,'2022-12-04',2,1),(23,'2022-12-04',2,1),(26,'2022-12-04',4,2),(27,'2022-12-04',3,1),(28,'2022-12-04',1,1),(33,'2022-12-05',3,1),(34,'2022-12-05',2,1),(35,'2022-12-06',2,3),(36,'2022-12-06',2,2),(37,'2022-12-07',1,1),(38,'2022-12-07',1,1),(45,'2022-12-07',2,1),(46,'2022-12-07',2,1),(47,'2022-12-07',2,1),(48,'2022-12-07',1,1),(49,'2022-12-07',1,1),(50,'2022-12-07',2,1),(51,'2022-12-07',4,2),(52,'2022-12-08',3,1),(53,'2022-12-08',1,1),(54,'2022-12-09',1,1),(55,'2022-12-09',1,1);
/*!40000 ALTER TABLE `ordering` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report`
--

DROP TABLE IF EXISTS `report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report` (
  `id_rep` int NOT NULL AUTO_INCREMENT,
  `year` int DEFAULT NULL,
  `month` int DEFAULT NULL,
  `id_dish` int DEFAULT NULL,
  `dish_count` int DEFAULT NULL,
  `month_income` int DEFAULT NULL,
  PRIMARY KEY (`id_rep`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report`
--

LOCK TABLES `report` WRITE;
/*!40000 ALTER TABLE `report` DISABLE KEYS */;
INSERT INTO `report` VALUES (40,2020,3,1,3,2000),(41,2020,3,2,1,450),(42,2020,3,3,1,480),(43,2020,3,4,1,400),(44,2020,3,6,3,1500),(45,2022,3,4,24,2000),(46,2022,11,1,6,1000),(47,2022,11,2,1,450),(48,2022,11,3,3,960),(49,2022,11,4,1,400),(50,2022,12,1,8,3000),(51,2022,12,2,4,1350),(52,2022,12,3,2,960),(53,2022,12,4,4,1600),(54,2022,12,5,1,600);
/*!40000 ALTER TABLE `report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_waiter`
--

DROP TABLE IF EXISTS `report_waiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `report_waiter` (
  `id_rep` int NOT NULL AUTO_INCREMENT,
  `year` int DEFAULT NULL,
  `month` int DEFAULT NULL,
  `Waiter_id_W` int DEFAULT NULL,
  `summa` int DEFAULT NULL,
  PRIMARY KEY (`id_rep`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_waiter`
--

LOCK TABLES `report_waiter` WRITE;
/*!40000 ALTER TABLE `report_waiter` DISABLE KEYS */;
INSERT INTO `report_waiter` VALUES (1,2022,12,1,9340),(2,2022,12,2,3100),(3,2022,12,3,980);
/*!40000 ALTER TABLE `report_waiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table`
--

DROP TABLE IF EXISTS `table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table` (
  `id_T` int NOT NULL,
  `chair` int DEFAULT NULL,
  `booking` tinyint DEFAULT NULL,
  `zone_id_z` int DEFAULT NULL,
  PRIMARY KEY (`id_T`),
  KEY `zone_id_z_idx` (`zone_id_z`),
  CONSTRAINT `zone_id_z` FOREIGN KEY (`zone_id_z`) REFERENCES `zone` (`id_z`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table`
--

LOCK TABLES `table` WRITE;
/*!40000 ALTER TABLE `table` DISABLE KEYS */;
INSERT INTO `table` VALUES (1,3,1,1),(2,2,0,1),(3,3,0,2),(4,2,0,2);
/*!40000 ALTER TABLE `table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v`
--

DROP TABLE IF EXISTS `v`;
/*!50001 DROP VIEW IF EXISTS `v`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v` AS SELECT 
 1 AS `id_M`,
 1 AS `name_dishes`,
 1 AS `count_M`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `waiter`
--

DROP TABLE IF EXISTS `waiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `waiter` (
  `id_W` int NOT NULL,
  `Passport` varchar(45) DEFAULT NULL,
  `Date_of_adm` date NOT NULL,
  `Date_of_dism` date DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `birthday` date NOT NULL,
  `name` varchar(45) NOT NULL,
  `surname` varchar(45) NOT NULL,
  PRIMARY KEY (`id_W`),
  UNIQUE KEY `Passport_UNIQUE` (`Passport`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waiter`
--

LOCK TABLES `waiter` WRITE;
/*!40000 ALTER TABLE `waiter` DISABLE KEYS */;
INSERT INTO `waiter` VALUES (1,'4616 404074','2020-10-05',NULL,20000,'2002-10-13','Андрей','Никольский'),(2,'3453 480345','2020-06-04',NULL,20000,'2002-09-16','Олег','Макаренко'),(3,'8465 463956','2020-09-13',NULL,20000,'2002-11-12','Виталий','Каменев'),(4,'2056 395018','2020-09-19',NULL,20000,'2002-02-01','Игорь','Зиновьев');
/*!40000 ALTER TABLE `waiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zone`
--

DROP TABLE IF EXISTS `zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zone` (
  `id_z` int NOT NULL,
  `Tables` int NOT NULL,
  `VIP` int DEFAULT NULL,
  `Smoker` tinyint DEFAULT NULL,
  PRIMARY KEY (`id_z`),
  UNIQUE KEY `VIP_UNIQUE` (`VIP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zone`
--

LOCK TABLES `zone` WRITE;
/*!40000 ALTER TABLE `zone` DISABLE KEYS */;
INSERT INTO `zone` VALUES (1,4,NULL,0),(2,4,NULL,1);
/*!40000 ALTER TABLE `zone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `v`
--

/*!50001 DROP VIEW IF EXISTS `v`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v` AS select `menu`.`id_M` AS `id_M`,`menu`.`name_dishes` AS `name_dishes`,count(`ol`.`Menu_id_M`) AS `count_M` from ((`menu` join `order_lines` `ol` on((`ol`.`Menu_id_M` = `menu`.`id_M`))) join `ordering` `ord` on((`ol`.`Ordering_id_O` = `ord`.`id_O`))) where (`ord`.`order_date` like '2020-03%') group by `menu`.`id_M`,`menu`.`name_dishes` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-22  8:09:19
