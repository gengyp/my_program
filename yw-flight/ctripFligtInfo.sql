/*
Navicat MySQL Data Transfer

Source Server         : 192.168.36.80
Source Server Version : 50720
Source Host           : 192.168.36.80:3306
Source Database       : apiDB

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2017-11-22 09:31:58
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ctripfligtinfo
-- ----------------------------
DROP TABLE IF EXISTS `ctripfligtinfo`;
CREATE TABLE `ctripfligtinfo` (
  `date` date DEFAULT NULL,
  `flightNo` varchar(11) DEFAULT NULL,
  `leaveAirport` varchar(255) DEFAULT NULL,
  `arriveAirport` varchar(255) DEFAULT NULL,
  `planTakeoffTime` varchar(20) DEFAULT NULL,
  `planLandingTime` varchar(255) DEFAULT NULL,
  `forcastTakeoffTime` varchar(20) DEFAULT NULL,
  `forcastLandingTime` varchar(20) DEFAULT NULL,
  `realTakeoffTime` varchar(20) DEFAULT NULL,
  `realLandingTime` varchar(20) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
