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

 Date: 02/10/2018 20:22:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for ANALYSIS_TM_MAIN_DATA
-- ----------------------------
DROP TABLE IF EXISTS `ANALYSIS_TM_MAIN_DATA`;
CREATE TABLE `ANALYSIS_TM_MAIN_DATA` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `DT` varchar(20) DEFAULT NULL,
  `RED_BALL` varchar(100) DEFAULT NULL,
  `BLUE_BALL` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1647 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
