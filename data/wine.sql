/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80300 (8.3.0)
 Source Host           : localhost:3306
 Source Schema         : wine

 Target Server Type    : MySQL
 Target Server Version : 80300 (8.3.0)
 File Encoding         : 65001

 Date: 29/10/2024 22:36:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for chat_log
-- ----------------------------
DROP TABLE IF EXISTS `chat_log`;
CREATE TABLE `chat_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `create_time` datetime DEFAULT NULL,
  `stage` int unsigned DEFAULT '0',
  `user_content` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `flat_content` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of chat_log
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `token` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `star` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `desc` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `wine_id` int unsigned DEFAULT '0',
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of score
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for wine
-- ----------------------------
DROP TABLE IF EXISTS `wine`;
CREATE TABLE `wine` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `year` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `create_time` datetime DEFAULT NULL,
  `desc` varchar(255) COLLATE utf8mb4_general_ci DEFAULT '',
  `price` int unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of wine
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
