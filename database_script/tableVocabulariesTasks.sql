CREATE SCHEMA `etls` ;

CREATE TABLE `etls`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `uuid` CHAR(40) NOT NULL,
  `type` ENUM('vocabulary', 'concepts') NOT NULL,
  `status` ENUM('Pending', 'Running', 'Succeeded', 'Failed') NOT NULL,
  `file_id` CHAR(100) NOT NULL,
  `date` DATETIME NOT NULL,
  `last_update_date` DATETIME NULL,
  PRIMARY KEY (`id`)
);