-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mystore
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mystore
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mystore` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `mystore` ;

-- -----------------------------------------------------
-- Table `mystore`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mystore`.`category` (
  `cat_id` INT NOT NULL AUTO_INCREMENT,
  `cat_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE INDEX `cat_id_UNIQUE` (`cat_id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mystore`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mystore`.`customer` (
  `cus_id` INT NOT NULL AUTO_INCREMENT,
  `cus_name` VARCHAR(45) NOT NULL,
  `cus_gender` VARCHAR(6) NOT NULL,
  `cus_birth` DATE NOT NULL,
  PRIMARY KEY (`cus_id`),
  UNIQUE INDEX `cust_id_UNIQUE` (`cus_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mystore`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mystore`.`product` (
  `prod_id` INT NOT NULL AUTO_INCREMENT,
  `prod_name` VARCHAR(45) NOT NULL,
  `prod_price` INT NOT NULL,
  `cat_id` INT NOT NULL,
  `prod_discount` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`prod_id`),
  UNIQUE INDEX `pd_id_UNIQUE` (`prod_id` ASC) VISIBLE,
  INDEX `cat_id_idx` (`cat_id` ASC) VISIBLE,
  CONSTRAINT `cat_id`
    FOREIGN KEY (`cat_id`)
    REFERENCES `mystore`.`category` (`cat_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mystore`.`transaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mystore`.`transaction` (
  `bsk_id` INT NOT NULL,
  `pd_id` INT NOT NULL,
  `qty` INT NOT NULL,
  `date` DATE NOT NULL,
  `hour` VARCHAR(2) NOT NULL,
  `cust_id` INT NOT NULL,
  INDEX `pd_id_idx` (`pd_id` ASC) VISIBLE,
  INDEX `cust_id_idx` (`cust_id` ASC) VISIBLE,
  CONSTRAINT `cust_id`
    FOREIGN KEY (`cust_id`)
    REFERENCES `mystore`.`customer` (`cus_id`),
  CONSTRAINT `pd_id`
    FOREIGN KEY (`pd_id`)
    REFERENCES `mystore`.`product` (`prod_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
