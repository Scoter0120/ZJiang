/*
 Navicat Premium Data Transfer

 Source Server         : Local_Mysql
 Source Server Type    : MySQL
 Source Server Version : 50722
 Source Host           : localhost:3306
 Source Schema         : ZJiang

 Target Server Type    : MySQL
 Target Server Version : 50722
 File Encoding         : 65001

 Date: 02/10/2018 20:22:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ANALYSIS_TA_DATA_RESULT
-- ----------------------------
DROP TABLE IF EXISTS `ANALYSIS_TA_DATA_RESULT`;
CREATE TABLE `ANALYSIS_TA_DATA_RESULT` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DT` varchar(20) DEFAULT NULL,
  `SOURCE_DATA` varchar(50) DEFAULT NULL,
  `RED_S_BALL` int(5) DEFAULT NULL,
  `BLUE_BALL` int(5) DEFAULT NULL,
  `CHA` varchar(50) DEFAULT NULL,
  `HE` int(11) DEFAULT NULL,
  `JI` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
