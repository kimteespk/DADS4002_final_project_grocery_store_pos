-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: mystore
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `cat_id` int NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(45) NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE KEY `cat_id_UNIQUE` (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Meat & Fish'),(2,'Dairy'),(3,'Vegetables and fruit'),(4,'Frozen Dessert'),(5,'Bread & Bread spreads'),(6,'Dried Goods'),(7,'Snacks'),(8,'Care Products'),(9,'Drinks'),(10,'Food');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cus_id` int NOT NULL AUTO_INCREMENT,
  `cus_name` varchar(45) NOT NULL,
  `cus_gender` varchar(6) DEFAULT NULL,
  `cus_birth` date DEFAULT NULL,
  PRIMARY KEY (`cus_id`),
  UNIQUE KEY `cust_id_UNIQUE` (`cus_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (0,'Anonymous',NULL,NULL),(1,'Harry Potter','male','1992-05-19'),(2,'Peter Parker','male','1994-04-10'),(3,'Hatrick Billson','male','1982-07-03'),(4,'Lee Kung','male','1988-04-05'),(5,'Francais De Lasere','male','1978-10-30'),(6,'Gwen Stacy','female','1994-06-21'),(7,'Nattarikan Jaijai','female','2005-09-29'),(8,'Nuntida Srisawan','female','2005-01-02'),(9,'Alisa Johanson','female','2004-03-20'),(10,'Jetsada Sawangwong','male','2004-05-11'),(11,'Sakkarin Srisai','male','2005-05-11'),(12,'Jirayu Hongthong','male','2000-01-28'),(13,'Khemanit Wongmalai','female','2000-01-14'),(14,'Jennifer Jang','female','1991-09-09'),(15,'Kim Saehyun','male','1994-10-09'),(16,'Saori Susano','male','1994-10-09'),(17,'Chayada Meejai','female','2001-08-08'),(18,'Danai Somprasong','male','1992-05-19'),(19,'Thidarat Somprasong','female','2004-03-20'),(20,'Somchai Jaidee','male','1978-10-30'),(21,'Passakorn Thongtham','male','1977-12-04'),(22,'Phichai Yoon','male','1977-06-12'),(23,'Richard Brooklin','male','1981-02-01'),(24,'Steven Hammer','male','1993-04-04'),(25,'Nuchanart Boonsong','female','2004-06-16'),(26,'Sasithorn Jaingarm','female','2000-12-04'),(27,'Park Jeesong','male','1991-11-01'),(28,'Lee Dongsan','male','1988-04-05'),(29,'Pim Valentine','female','2001-05-13'),(30,'Polla Dolsen','female','1994-03-13'),(31,'Nicolas Frankfirts','male','1992-07-18'),(32,'Eddy Maccuffin','male','1989-09-15'),(33,'Michael Nelson','female','1991-10-10'),(34,'Nungruetai Fuengfu','female','1994-06-21'),(35,'Phakkawan Iamong','female','2005-09-29');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `prod_id` int NOT NULL AUTO_INCREMENT,
  `prod_name` varchar(45) NOT NULL,
  `prod_price` float NOT NULL,
  `cat_id` int NOT NULL,
  `prod_discount` float DEFAULT NULL,
  PRIMARY KEY (`prod_id`),
  UNIQUE KEY `pd_id_UNIQUE` (`prod_id`),
  KEY `cat_id_idx` (`cat_id`),
  CONSTRAINT `cat_id` FOREIGN KEY (`cat_id`) REFERENCES `category` (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Lay\'s',20,7,0.9),(2,'Sunbite',20,7,0.9),(3,'Testo',20,7,0.85),(4,'Chili Sauce',59,6,0.76),(5,'Durian Chips',200,7,0.97),(6,'Mixed Fruit Ice Cream',25,4,0.8),(7,'Mixed Vegetables',49,3,0.81),(8,'chinese steamed dumplings',29,10,0.86),(9,'Frozen Fried Chicken',49,10,0.96),(10,'Tuna Salad',50,10,0.9),(11,'Salmon',590,1,0.98),(12,'Yogurt',25,2,0.84),(13,'Shrimp and Basil Fried Rice',45,1,0.95),(14,'Chocolate Bar',15,7,0.8),(15,'Croissant',25,5,0.76),(16,'Frozen Squid',89,1,0.9),(17,'Blueberry Jam',49,6,0.79),(18,'Frozen French Fried',99,10,0.9),(19,'Sunblock Cream',390,8,0.89),(20,'Vitamin C',390,8,0.94),(21,'Cleansing Face Cream',290,8,0.84),(22,'Fresh Eggs 10 Pcs',55,1,0.89),(23,'Whey Protein 6 lbs',1100,6,0.95),(24,'Pickled White Radish',85,3,0.92),(25,'Greek Yogurt',69,2,0.94),(26,'Oat Drinks Deluxe',125,2,0.95),(27,'Vanilla Ice Cream',49,4,0.91),(28,'Mochi Ice Cream',20,4,0.9),(29,'Egg Tart',22,5,0.9),(30,'Chocolate Chip Cookies',25,5,0.76),(31,'Thompson Seedless Grapes',200,3,0.94);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `bsk_id` int NOT NULL,
  `prod_id` int NOT NULL,
  `qty` int NOT NULL,
  `date` date NOT NULL,
  `hour` int NOT NULL,
  `cus_id` int DEFAULT NULL,
  KEY `pd_id_idx` (`prod_id`),
  KEY `cus_id_idx` (`cus_id`),
  CONSTRAINT `cus_id` FOREIGN KEY (`cus_id`) REFERENCES `customer` (`cus_id`),
  CONSTRAINT `pd_id` FOREIGN KEY (`prod_id`) REFERENCES `product` (`prod_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (120,5,2,'2019-07-24',17,NULL),(121,19,6,'2023-05-09',7,NULL),(122,22,6,'2021-01-24',15,NULL),(123,7,7,'2019-03-02',21,NULL),(124,22,3,'2023-10-03',5,NULL),(125,21,4,'2020-11-04',4,NULL),(126,12,2,'2020-03-24',2,NULL),(127,2,5,'2019-11-30',15,NULL),(128,20,6,'2020-11-18',22,NULL),(129,24,7,'2022-10-26',20,NULL),(130,10,3,'2021-09-01',5,NULL),(131,14,2,'2022-01-24',2,NULL),(132,25,3,'2023-12-07',16,NULL),(133,28,3,'2020-05-01',18,NULL),(134,17,6,'2019-10-20',7,NULL),(135,6,6,'2021-06-30',6,NULL),(136,26,1,'2020-05-04',3,NULL),(137,7,6,'2021-12-06',23,NULL),(138,27,5,'2021-08-18',15,NULL),(139,24,7,'2022-09-13',18,NULL),(140,6,2,'2019-08-23',1,NULL),(141,13,2,'2023-01-22',4,NULL),(142,6,1,'2022-08-03',18,NULL),(143,25,5,'2022-03-23',0,NULL),(144,3,2,'2023-03-29',11,NULL),(145,1,1,'2021-08-06',19,NULL),(146,5,3,'2023-08-30',23,NULL),(147,16,3,'2021-01-28',14,NULL),(148,30,6,'2021-06-25',21,NULL),(149,10,1,'2019-01-29',2,NULL),(150,27,3,'2020-04-10',15,NULL),(151,30,6,'2023-08-09',19,NULL),(152,10,5,'2022-06-20',23,NULL),(153,2,4,'2022-07-18',21,NULL),(154,4,2,'2023-01-06',3,NULL),(155,13,6,'2020-03-10',14,NULL),(156,25,4,'2023-04-13',4,NULL),(157,9,7,'2023-06-07',19,NULL),(158,19,3,'2023-07-11',15,NULL),(159,2,6,'2019-09-22',11,NULL),(160,4,2,'2020-11-05',6,NULL),(161,18,5,'2021-08-10',9,NULL),(162,12,7,'2020-01-14',11,NULL),(163,27,1,'2020-02-10',19,NULL),(164,31,5,'2023-05-10',22,NULL),(165,23,7,'2020-06-23',19,NULL),(166,28,7,'2023-10-08',22,NULL),(167,16,2,'2021-07-16',7,NULL),(168,30,5,'2023-08-07',5,NULL),(169,29,7,'2020-02-16',18,NULL),(170,1,1,'2022-01-28',9,NULL),(171,21,3,'2023-12-22',4,NULL),(172,28,5,'2019-04-19',17,NULL),(173,12,5,'2022-04-22',15,NULL),(174,24,5,'2022-10-18',8,NULL),(175,29,2,'2019-07-05',6,NULL),(176,10,7,'2022-07-16',16,NULL),(177,18,6,'2023-01-14',11,NULL),(178,29,2,'2021-12-13',8,NULL),(179,4,4,'2020-11-28',13,NULL),(180,4,6,'2019-02-27',16,NULL),(181,24,1,'2022-06-07',17,NULL),(182,20,7,'2019-09-19',2,NULL),(183,27,7,'2021-06-26',5,NULL),(184,15,7,'2019-09-13',9,NULL),(185,5,6,'2022-06-08',22,NULL),(186,12,3,'2020-05-11',4,NULL),(187,17,4,'2019-09-24',9,NULL),(188,22,6,'2020-04-17',17,NULL),(189,7,7,'2022-06-27',23,NULL),(190,29,6,'2022-01-19',21,NULL),(191,20,1,'2019-05-03',8,NULL),(192,25,7,'2023-05-27',6,NULL),(193,24,1,'2022-09-11',18,NULL),(194,21,2,'2021-02-21',0,NULL),(195,19,2,'2020-09-16',4,NULL),(196,31,4,'2021-07-12',23,NULL),(197,11,1,'2021-09-09',12,NULL),(198,7,5,'2022-08-15',13,NULL),(199,5,4,'2022-11-21',10,NULL),(200,9,3,'2022-09-02',0,NULL),(201,9,6,'2019-03-13',17,NULL),(202,12,3,'2021-06-18',18,NULL),(203,30,3,'2023-03-09',0,NULL),(204,26,5,'2022-09-23',14,NULL),(205,6,2,'2020-06-29',20,NULL),(206,13,5,'2021-12-20',20,NULL),(207,12,5,'2021-07-10',3,NULL),(208,13,1,'2021-03-08',23,NULL),(209,25,6,'2023-06-01',16,NULL),(210,27,3,'2020-10-14',14,NULL),(211,21,3,'2022-02-12',21,NULL),(212,30,1,'2021-06-15',1,NULL),(213,11,2,'2021-04-20',12,NULL),(214,10,5,'2022-09-19',7,NULL),(215,9,6,'2022-08-04',4,NULL),(216,14,2,'2023-05-30',6,NULL),(217,4,2,'2020-10-30',11,NULL),(218,20,3,'2020-02-08',18,NULL),(219,12,1,'2019-09-20',15,NULL),(1,26,3,'2023-07-29',2,35),(2,15,4,'2019-08-06',2,30),(3,19,2,'2020-10-02',9,35),(4,24,7,'2021-12-24',9,23),(5,28,3,'2021-08-24',5,23),(6,19,7,'2022-06-13',12,8),(7,22,5,'2021-02-08',10,9),(8,5,1,'2020-10-11',11,24),(9,24,3,'2023-08-03',23,34),(10,21,3,'2023-02-24',21,8),(11,14,2,'2019-04-13',21,12),(12,12,6,'2021-07-22',1,9),(13,10,5,'2022-02-15',11,35),(14,26,1,'2023-08-13',2,22),(15,15,2,'2019-09-07',21,2),(16,16,3,'2023-06-18',10,5),(17,31,1,'2021-02-16',22,26),(18,21,6,'2019-04-21',16,26),(19,13,3,'2023-02-25',18,17),(20,30,6,'2020-11-24',18,9),(21,12,7,'2020-01-02',19,17),(22,30,4,'2021-12-17',6,17),(23,12,3,'2019-04-25',13,30),(24,2,6,'2022-09-08',21,13),(25,24,1,'2020-03-10',10,21),(26,4,4,'2020-12-15',4,27),(27,25,2,'2023-01-10',19,21),(28,5,1,'2023-06-02',18,27),(29,20,1,'2022-09-22',7,16),(30,30,4,'2022-05-13',10,7),(31,28,4,'2020-10-02',19,28),(32,22,5,'2023-12-27',15,13),(33,3,5,'2021-10-31',18,8),(34,22,4,'2023-08-10',14,16),(35,15,7,'2023-07-16',0,7),(36,28,5,'2022-09-22',5,16),(37,24,4,'2021-06-14',11,12),(38,11,7,'2022-11-24',1,20),(39,9,5,'2022-03-10',9,5),(40,30,7,'2021-05-01',22,13),(41,18,1,'2019-04-08',19,5),(42,4,1,'2019-09-30',0,10),(43,23,2,'2021-10-13',16,27),(44,24,3,'2021-05-19',18,29),(45,25,2,'2021-02-06',5,29),(46,4,6,'2021-12-19',3,29),(47,8,7,'2022-01-30',16,7),(48,18,4,'2019-07-11',18,3),(49,30,1,'2020-10-10',13,13),(50,27,6,'2022-02-02',1,19),(51,1,1,'2021-01-04',7,14),(52,12,3,'2019-11-17',10,16),(53,4,4,'2021-06-15',23,13),(54,10,7,'2019-10-29',11,3),(55,31,2,'2021-05-09',17,13),(56,27,2,'2021-07-07',21,22),(57,18,4,'2023-02-17',13,15),(58,1,6,'2023-07-28',13,27),(59,28,6,'2021-03-22',4,23),(60,23,7,'2019-08-28',9,20),(61,6,7,'2022-08-28',18,20),(62,2,1,'2019-02-25',7,27),(63,23,6,'2023-11-25',18,3),(64,18,7,'2019-10-17',2,17),(65,25,7,'2021-04-24',2,35),(66,14,3,'2019-08-23',3,1),(67,9,6,'2019-07-09',18,9),(68,18,6,'2021-09-20',2,2),(69,8,6,'2021-09-14',1,6),(70,25,5,'2019-11-30',4,14),(71,5,5,'2023-04-24',3,34),(72,27,6,'2019-08-12',17,28),(73,4,6,'2020-11-10',17,15),(74,9,6,'2022-10-08',12,8),(75,23,7,'2023-06-21',16,12),(76,28,7,'2020-11-17',1,6),(77,15,5,'2022-10-01',0,6),(78,25,4,'2021-05-31',11,6),(79,22,4,'2020-02-25',23,31),(80,9,6,'2021-12-28',22,14),(81,24,6,'2023-09-24',2,17),(82,7,5,'2023-11-17',23,23),(83,22,2,'2023-04-30',6,29),(84,3,4,'2020-02-06',12,27),(85,6,7,'2023-12-11',19,27),(86,21,7,'2023-12-09',1,34),(87,31,3,'2023-12-23',23,6),(88,23,2,'2020-05-10',13,10),(89,15,3,'2022-01-11',1,25),(90,19,4,'2023-09-03',10,20),(91,25,3,'2022-02-13',22,4),(92,14,6,'2022-04-13',2,13),(93,7,7,'2021-12-27',18,7),(94,22,6,'2022-11-15',3,13),(95,11,3,'2021-08-17',2,6),(96,20,3,'2022-12-05',6,29),(97,3,6,'2019-03-23',2,17),(98,1,6,'2019-08-05',10,23),(99,12,1,'2020-12-08',22,34),(100,30,4,'2022-06-06',0,10),(101,29,4,'2022-09-07',7,26),(102,26,4,'2020-10-13',16,27),(103,25,4,'2021-11-03',17,26),(104,23,4,'2023-07-04',0,13),(105,23,6,'2021-05-12',7,5),(106,20,2,'2020-11-22',13,20),(107,2,4,'2021-01-01',9,12),(108,7,3,'2023-11-11',1,12),(109,15,7,'2020-02-07',2,35),(110,24,4,'2020-12-15',15,6),(111,14,4,'2019-05-31',14,20),(112,19,4,'2022-02-06',11,35),(113,31,7,'2019-10-11',4,13),(114,21,4,'2023-07-03',20,4),(115,14,1,'2023-10-11',6,13),(116,6,6,'2019-11-24',2,5),(117,11,4,'2019-12-18',20,35),(118,27,1,'2022-05-06',0,3),(119,1,6,'2023-07-06',15,31);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-23 13:49:27
