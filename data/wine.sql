/*
 Navicat Premium Data Transfer

 Source Server         : 本地
 Source Server Type    : MySQL
 Source Server Version : 80040 (8.0.40)
 Source Host           : localhost:3306
 Source Schema         : wine

 Target Server Type    : MySQL
 Target Server Version : 80040 (8.0.40)
 File Encoding         : 65001

 Date: 30/10/2024 18:17:14
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for chat_log
-- ----------------------------
DROP TABLE IF EXISTS `chat_log`;
CREATE TABLE `chat_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `token` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `create_time` datetime DEFAULT NULL,
  `stage` int unsigned DEFAULT '0',
  `user_content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `flat_content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
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
  `token` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `star` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
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
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `year` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `create_time` datetime DEFAULT NULL,
  `desc` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT '',
  `price` int unsigned DEFAULT '0',
  `wine_id` int DEFAULT NULL,
  `intent` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of wine
-- ----------------------------
BEGIN;
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (1, '拉菲红酒', '2015', '2023-01-15 12:30:45', '口感柔和，带有细腻的果香和微妙的橡木气息，余味悠长。', 150, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (2, '玛歌红酒', '2016', '2023-02-10 15:45:23', '香气丰富，入口圆润，有明显的黑醋栗和李子味道。', 180, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (3, '罗曼尼康帝', '2014', '2023-01-20 13:15:32', '层次复杂，带有浓郁的花香和果香，口感丝滑。', 250, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (4, '柏图斯', '2018', '2023-03-05 18:22:11', '口感丰厚，单宁柔和，伴有黑莓和香草的味道。', 300, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (5, '作品一号', '2017', '2023-02-14 16:20:10', '风味浓郁，带有黑莓和黑樱桃的香气，结构饱满。', 220, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (6, '木桐红酒', '2016', '2023-01-19 14:35:54', '酒体平衡，口感圆润，带有一丝香料和烟熏味。', 210, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (7, '尖叫鹰', '2019', '2023-02-28 19:12:45', '浓郁果香，伴随丝滑的单宁和巧克力的余韵。', 320, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (8, '伊甘酒庄', '2018', '2023-03-01 12:44:37', '香甜可口，带有蜂蜜和杏仁的味道，口感饱满。', 280, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (9, '奔富葛兰许', '2015', '2023-02-07 11:32:14', '果香浓郁，伴有一丝泥土气息，余味悠长。', 170, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (10, '西施佳雅', '2017', '2023-03-12 17:15:55', '丝滑而优雅，带有红浆果和香料的香气。', 210, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (11, '天娜红酒', '2016', '2023-01-25 13:55:29', '香气丰富，有红色水果和香料的复杂风味。', 120, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (12, '贝加西利亚', '2014', '2023-02-15 15:22:03', '口感细腻，伴随花香和香草的味道。', 260, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (13, '嘉雅巴巴莱斯科', '2018', '2023-03-11 16:33:41', '酸度适中，带有明显的红色水果味道。', 150, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (14, '侯伯王红酒', '2017', '2023-01-26 12:08:56', '带有石墨和烟熏的香气，口感浓郁。', 200, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (15, '拉图红酒', '2016', '2023-02-18 18:44:21', '风味浓厚，单宁扎实，余味悠长。', 220, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (16, '乐王吉', '2015', '2023-03-03 11:49:37', '深沉的口感，带有浓厚的黑醋栗和李子味。', 290, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (17, '阿玛维雅', '2017', '2023-01-17 16:22:14', '香气细腻，单宁柔和，带有丝滑的回味。', 160, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (18, '菲尔普斯传世珍酿', '2019', '2023-03-07 13:15:47', '丰富的黑莓和巧克力香气，口感饱满。', 230, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (19, '伊瑟尔酒园', '2018', '2023-01-28 12:42:36', '口感优雅，伴有矿物质的清新感。', 240, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (20, '碧尚男爵', '2014', '2023-02-25 17:08:32', '顺滑的口感，黑色水果风味浓厚。', 140, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (21, '塔特红酒', '2015', '2023-01-22 14:15:20', '红色浆果的浓郁香气，口感圆润饱满。', 170, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (22, '爱士图尔', '2016', '2023-03-13 11:54:18', '酒体丰腴，有明显的黑醋栗和香草味。', 200, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (23, '梦玫瑰', '2018', '2023-01-30 10:25:44', '酒体饱满，余味悠长，带有深色水果的香气。', 190, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (24, '达尔图酒庄', '2019', '2023-02-27 14:35:01', '复杂的层次感，带有轻微的泥土气息。', 180, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (25, '贝尔优酒庄', '2017', '2023-03-10 16:50:29', '果香浓郁，口感平衡且圆润。', 130, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (26, '柏菲酒庄', '2015', '2023-01-31 18:21:12', '浓郁的黑加仑和咖啡香气，回味悠长。', 220, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (27, '靓茨伯酒庄', '2016', '2023-02-08 13:30:33', '单宁柔和，带有烟熏和香草的风味。', 160, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (28, '鲁臣世家', '2014', '2023-01-13 11:11:45', '酒体平衡，有淡淡的草本气息。', 140, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (29, '宝嘉龙', '2017', '2023-03-02 15:05:12', '口感顺滑，红色水果风味浓郁。', 150, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (30, '都夏美隆', '2018', '2023-01-21 17:38:06', '酒体饱满，带有泥土和黑莓的味道。', 175, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (31, '塔尔博', '2019', '2023-02-11 16:29:52', '层次丰富，伴随红色水果的香气。', 125, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (32, '白马庄', '2015', '2023-02-04 12:07:21', '黑醋栗和香料的香气，口感细腻。', 140, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (33, '姬斯库酒庄', '2016', '2023-03-08 13:43:58', '带有樱桃和香料的味道，余味悠长。', 155, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (34, '坎特纳克', '2014', '2023-01-18 11:58:47', '酒体平衡，带有花香和水果的香气。', 135, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (35, '拉格朗酒庄', '2017', '2023-02-23 12:11:39', '果香清新，带有浆果的余韵。', 145, NULL, NULL);
INSERT INTO `wine` (`id`, `name`, `year`, `create_time`, `desc`, `price`, `wine_id`, `intent`) VALUES (36, '拉萨尔酒庄', '2018', '2023-03-06 17:20:31', '圆润柔和，红色浆果和香料香气丰富。', 160, NULL, NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
