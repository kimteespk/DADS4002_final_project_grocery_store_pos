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
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE INDEX `cat_id_UNIQUE` (`cat_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mystore`.`customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mystore`.`customer` (
  `cust_id` INT NOT NULL AUTO_INCREMENT,
  `gender` VARCHAR(1) NOT NULL,
  `birth_date` DATE NOT NULL,
  `firstname` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cust_id`),
  UNIQUE INDEX `cust_id_UNIQUE` (`cust_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `mystore`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mystore`.`product` (
  `pd_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `price` INT NOT NULL,
  `cat_id` INT NOT NULL,
  `discount` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`pd_id`),
  UNIQUE INDEX `pd_id_UNIQUE` (`pd_id` ASC) VISIBLE,
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
  `basket_id` INT NOT NULL,
  `pd_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `date` DATE NOT NULL,
  `hour` VARCHAR(2) NOT NULL,
  `cust_id` INT NOT NULL,
  INDEX `pd_id_idx` (`pd_id` ASC) VISIBLE,
  INDEX `cust_id_idx` (`cust_id` ASC) VISIBLE,
  CONSTRAINT `cust_id`
    FOREIGN KEY (`cust_id`)
    REFERENCES `mystore`.`customer` (`cust_id`),
  CONSTRAINT `pd_id`
    FOREIGN KEY (`pd_id`)
    REFERENCES `mystore`.`product` (`pd_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
