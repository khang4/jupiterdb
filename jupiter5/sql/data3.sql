-- MySQL dump 10.13  Distrib 5.6.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: jupiter
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (0,1,'fish'),(0,2,'teal'),(0,3,'sea'),(0,4,'something philosophical'),(0,5,'we are the ground'),(0,6,'we are the earth'),(0,7,'yes'),(0,8,'no'),(0,9,'potentially'),(1,1,'dolphines'),(1,2,'white'),(1,3,'trees'),(1,4,'a poem'),(1,6,'we are not the earth'),(1,7,'but of course'),(1,8,'are you mad??'),(1,9,'it\'s possible'),(2,1,'rivers'),(2,7,'why not'),(2,8,'monster!'),(2,9,'let me stop to consider'),(3,9,'give me more time to consider');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `appanswer`
--

LOCK TABLES `appanswer` WRITE;
/*!40000 ALTER TABLE `appanswer` DISABLE KEYS */;
INSERT INTO `appanswer` VALUES (1,1,'im not really sure, that\'s why i\'m studying whales, right? this answer should be good enough'),(1,3,'if i believe so, on this very earth?  if you would like me to elaborate, please contact me in a few days, i will be away for a while.  i\'m not doing any research or anything, hahA'),(1,10,'chicken nuggets? ha ha, isnt that a funny joke? do you wish you could just give me a correct score on this'),(1,11,'i suppose so');
/*!40000 ALTER TABLE `appanswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `applicants`
--

LOCK TABLES `applicants` WRITE;
/*!40000 ALTER TABLE `applicants` DISABLE KEYS */;
INSERT INTO `applicants` VALUES (1,'john','bobbo','bell','12 ab str','1919','fd','bobbo@g.com','m','1990-12-05'),(2,'memnas','holt','yuughy','789 hju ln','8976','kj','ho@g.com','m','1991-12-08'),(3,'mery','vlante','qwegh','yuugat rd','4587','er','mry@g.com','f','1994-05-30'),(4,'wetr','williams','fubnth','12 polk str','5677','wd','noawe@g.com','m','1993-02-05'),(5,'wessy','soide','qroth','88 ninty ln','9090','ty','uncreative@g.com','f','1993-07-16');
/*!40000 ALTER TABLE `applicants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `application`
--

LOCK TABLES `application` WRITE;
/*!40000 ALTER TABLE `application` DISABLE KEYS */;
INSERT INTO `application` VALUES (1,'whale studies',1,'sdfh89ashfsuaidhfuisdafh usdahfiudhfgui sdfgudfiguidfguihdfgh soidfhodsf gsd fgdiof gjpoidfhd fgio jhdfio hiodf gjhiodf jhodi gjhiodf ghoidf jhiodf hio dfgiohdfoigh dfgh df gh dfiog jhoidfpgjhdofpi gh dfg h fgiohjior gij iortj gdfggh d  dfigjh dopfi ghdfgjhiodf g','spring',2019,"","","");
/*!40000 ALTER TABLE `application` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `criteria`
--

LOCK TABLES `criteria` WRITE;
/*!40000 ALTER TABLE `criteria` DISABLE KEYS */;
INSERT INTO `criteria` VALUES (1,'whale studies','like blue'),(2,'whale studies','distaste for chicken nuggets'),(3,'paper','computer usage'),(4,'paper','amount od paper owned');
/*!40000 ALTER TABLE `criteria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `criteria_score`
--

LOCK TABLES `criteria_score` WRITE;
/*!40000 ALTER TABLE `criteria_score` DISABLE KEYS */;
INSERT INTO `criteria_score` VALUES (0,2,'a god amonst men','has destroyed over five hundred chicken nugget manufacturing installations'),(0,3,'acceptable','once a week'),(0,4,'very good','enough to fill three rooms'),(1,2,'very good','has despised nuggets since before they were born'),(1,3,'very good','doesn\'t own one'),(1,4,'acceptable','enough to drown in'),(2,2,'very good','participated in the protest against the invention of nuggets'),(2,3,'terrible','greater than three times a week'),(2,4,'poor','enough that a fire could start using a match'),(3,2,'poor','has entered and tolerated the prescence of a nugget for >4 minutes'),(3,4,'slightly better than poor','enough that a fire could start, without a match or firestarting device'),(4,2,'very very poor','has consumed a chicken nugget'),(5,2,'immediately dismiss this applicant','has consumed greater than one chicken nugget'),(8,2,'acceptable','has heard of chicken nuggets, but does not yet know their significance to the field of whale studies');
/*!40000 ALTER TABLE `criteria_score` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `degree`
--

LOCK TABLES `degree` WRITE;
/*!40000 ALTER TABLE `degree` DISABLE KEYS */;
INSERT INTO `degree` VALUES ('paper','natural','ausd degh','asiod@j.com','936957376453',''),('skytology','earth department','neme addns','mad@j.com','9475012847',''),('whale studies','zoology','bill smit','asmt@j.com','1111111111','');
/*!40000 ALTER TABLE `degree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `education`
--

LOCK TABLES `education` WRITE;
/*!40000 ALTER TABLE `education` DISABLE KEYS */;
/*!40000 ALTER TABLE `education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `email`
--

LOCK TABLES `email` WRITE;
/*!40000 ALTER TABLE `email` DISABLE KEYS */;
/*!40000 ALTER TABLE `email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `gre`
--

LOCK TABLES `gre` WRITE;
/*!40000 ALTER TABLE `gre` DISABLE KEYS */;
/*!40000 ALTER TABLE `gre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `phone_number`
--

LOCK TABLES `phone_number` WRITE;
/*!40000 ALTER TABLE `phone_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `phone_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `requirement`
--

LOCK TABLES `requirement` WRITE;
/*!40000 ALTER TABLE `requirement` DISABLE KEYS */;
INSERT INTO `requirement` VALUES (1,'whale studies','what is a whale'),(2,'whale studies','what colour are whales'),(3,'whale studies','where do whales live'),(4,'skytology','where is the sky'),(5,'skytology','where is the ground'),(6,'skytology','where is earth'),(7,'paper','paper'),(8,'paper','not paper'),(9,'paper','tree'),(10,'whale studies','what are whales made of'),(11,'whale studies','are whales good');
/*!40000 ALTER TABLE `requirement` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-10 17:08:52
