/*
 Navicat Premium Data Transfer

 Source Server         : local
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : db1

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 20/06/2019 17:18:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `caption` char(32) NOT NULL DEFAULT '',
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of class
-- ----------------------------
BEGIN;
INSERT INTO `class` VALUES (1, '三年二班');
INSERT INTO `class` VALUES (2, '一年三班');
INSERT INTO `class` VALUES (3, '三年一班');
COMMIT;

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` char(32) NOT NULL DEFAULT '',
  `tearch_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`cid`),
  KEY `teacher_course` (`tearch_id`),
  CONSTRAINT `teacher_course` FOREIGN KEY (`tearch_id`) REFERENCES `teacher` (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------
BEGIN;
INSERT INTO `course` VALUES (1, '生物', 1);
INSERT INTO `course` VALUES (2, '体育', 1);
INSERT INTO `course` VALUES (3, '物理', 2);
COMMIT;

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `corse_id` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `student_score` (`student_id`),
  KEY `corse_score` (`corse_id`),
  CONSTRAINT `corse_score` FOREIGN KEY (`corse_id`) REFERENCES `course` (`cid`),
  CONSTRAINT `student_score` FOREIGN KEY (`student_id`) REFERENCES `student` (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of score
-- ----------------------------
BEGIN;
INSERT INTO `score` VALUES (1, 1, 1, 60);
INSERT INTO `score` VALUES (2, 1, 2, 59);
INSERT INTO `score` VALUES (3, 2, 2, 100);
COMMIT;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sname` char(32) NOT NULL DEFAULT '',
  `gender` char(6) NOT NULL DEFAULT '',
  `class_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`sid`),
  KEY `class_student` (`class_id`),
  CONSTRAINT `class_student` FOREIGN KEY (`class_id`) REFERENCES `class` (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES (1, '钢弹', '女', 1);
INSERT INTO `student` VALUES (2, '铁锤', '女', 1);
INSERT INTO `student` VALUES (3, '山炮', '男', 2);
COMMIT;

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `tname` char(32) NOT NULL DEFAULT '',
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
BEGIN;
INSERT INTO `teacher` VALUES (1, '波多');
INSERT INTO `teacher` VALUES (2, '苍空');
INSERT INTO `teacher` VALUES (3, '饭岛');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
