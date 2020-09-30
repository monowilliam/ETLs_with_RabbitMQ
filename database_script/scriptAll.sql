CREATE TABLE `vocabularies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ref` char(20) NOT NULL,
  `name` char(255) NOT NULL,
  `url` char(255) NOT NULL,
  `version` char(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `status` char(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

SELECT count(*) FROM myDB.concepts;

SELECT * FROM etls.tasks;
SELECT * FROM myDB.concepts;
SELECT * FROM myDB.vocabularies;

CREATE TABLE `concepts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pxordx` char(1) NULL,
  `oldpxordx` char(1) NULL,
  `codetype` char(3) NULL,
  `concept_class_id` char(80) NULL,
  `concept_id` int(11) NULL,
  `vocabulary_id` char(10) NULL,
  `domain_id` char(20) NULL,
  `track` char(20) NULL,
  `standard_concept` char(4) NULL,
  `code` char(20) NULL,
  `codewithperiods` char(10) NULL,
  `codescheme` char(10) NULL,
  `long_desc` varchar(500) NULL,
  `short_desc` varchar(500) NULL,
  `code_status` char(1) NULL,
  `code_change` char(10) NULL,
  `code_change_year` int(4) NULL,
  `code_planned_type` char(2) NULL,
  `code_billing_status` char(1) NULL,
  `code_cms_claim_status` char(1) NULL,
  `sex_cd` char(1) NULL,
  `anat_or_cond` char(1) NULL,
  `poa_code_status` char(1) NULL,
  `poa_code_change` char(10) NULL,
  `poa_code_change_year` int(4) NULL,
  `valid_start_date` int(11) NULL,
  `valid_end_date` int(11) NULL,
  `invalid_reason` char(10) NULL,
  `create_dt` int(11) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

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