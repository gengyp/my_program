/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : scraping

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2017-11-20 10:07:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for ctripairportname
-- ----------------------------
DROP TABLE IF EXISTS `ctripairportname`;
CREATE TABLE `ctripairportname` (
  `airportNo` int(11) NOT NULL,
  `nickName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ctripairportname
-- ----------------------------
INSERT INTO `ctripairportname` VALUES ('1', 'aletai');
INSERT INTO `ctripairportname` VALUES ('2', 'yiershi');
INSERT INTO `ctripairportname` VALUES ('3', 'kunsha');
INSERT INTO `ctripairportname` VALUES ('4', 'wulipu');
INSERT INTO `ctripairportname` VALUES ('5', 'akesu');
INSERT INTO `ctripairportname` VALUES ('6', 'tengao');
INSERT INTO `ctripairportname` VALUES ('7', 'tianzhushan');
INSERT INTO `ctripairportname` VALUES ('8', 'huangguoshu');
INSERT INTO `ctripairportname` VALUES ('9', 'alashanzuoqi');
INSERT INTO `ctripairportname` VALUES ('10', 'anyang');
INSERT INTO `ctripairportname` VALUES ('11', 'alashanyouqi');
INSERT INTO `ctripairportname` VALUES ('12', 'nanyuan');
INSERT INTO `ctripairportname` VALUES ('13', 'baise');
INSERT INTO `ctripairportname` VALUES ('14', 'erliban');
INSERT INTO `ctripairportname` VALUES ('15', 'feixiong');
INSERT INTO `ctripairportname` VALUES ('16', 'fucheng');
INSERT INTO `ctripairportname` VALUES ('17', 'bole');
INSERT INTO `ctripairportname` VALUES ('18', 'baoshan');
INSERT INTO `ctripairportname` VALUES ('19', 'shoudu');
INSERT INTO `ctripairportname` VALUES ('20', 'tianjitai');
INSERT INTO `ctripairportname` VALUES ('21', 'changbaishan');
INSERT INTO `ctripairportname` VALUES ('22', 'bangda');
INSERT INTO `ctripairportname` VALUES ('23', 'taohuayuan');
INSERT INTO `ctripairportname` VALUES ('24', 'longjia');
INSERT INTO `ctripairportname` VALUES ('25', 'chaoyang');
INSERT INTO `ctripairportname` VALUES ('26', 'yulong');
INSERT INTO `ctripairportname` VALUES ('27', 'changzhi');
INSERT INTO `ctripairportname` VALUES ('28', 'jiangbei');
INSERT INTO `ctripairportname` VALUES ('29', 'huanghua');
INSERT INTO `ctripairportname` VALUES ('30', 'shuangliu');
INSERT INTO `ctripairportname` VALUES ('31', 'jiayi');
INSERT INTO `ctripairportname` VALUES ('32', 'benniu');
INSERT INTO `ctripairportname` VALUES ('33', 'jiuhuashan');
INSERT INTO `ctripairportname` VALUES ('34', 'yongan');
INSERT INTO `ctripairportname` VALUES ('35', 'saertu');
INSERT INTO `ctripairportname` VALUES ('36', 'yungang');
INSERT INTO `ctripairportname` VALUES ('37', 'heshi');
INSERT INTO `ctripairportname` VALUES ('38', 'yading');
INSERT INTO `ctripairportname` VALUES ('39', 'langtou');
INSERT INTO `ctripairportname` VALUES ('40', 'xianggelila');
INSERT INTO `ctripairportname` VALUES ('41', 'zhoushuizi');
INSERT INTO `ctripairportname` VALUES ('42', 'dali');
INSERT INTO `ctripairportname` VALUES ('43', 'dunhuang');
INSERT INTO `ctripairportname` VALUES ('44', 'danyang');
INSERT INTO `ctripairportname` VALUES ('45', 'delingha');
INSERT INTO `ctripairportname` VALUES ('46', 'yijinhuoluo');
INSERT INTO `ctripairportname` VALUES ('47', 'taolai');
INSERT INTO `ctripairportname` VALUES ('48', 'xujiaping');
INSERT INTO `ctripairportname` VALUES ('49', 'saiwusu');
INSERT INTO `ctripairportname` VALUES ('50', 'changle');
INSERT INTO `ctripairportname` VALUES ('51', 'xiguan');
INSERT INTO `ctripairportname` VALUES ('52', 'shadi');
INSERT INTO `ctripairportname` VALUES ('53', 'dongji');
INSERT INTO `ctripairportname` VALUES ('54', 'fuyun');
INSERT INTO `ctripairportname` VALUES ('55', 'lianhuashan');
INSERT INTO `ctripairportname` VALUES ('56', 'huangjin');
INSERT INTO `ctripairportname` VALUES ('57', 'longdongbao');
INSERT INTO `ctripairportname` VALUES ('58', 'liangjiang');
INSERT INTO `ctripairportname` VALUES ('59', 'guanghua');
INSERT INTO `ctripairportname` VALUES ('60', 'baiyun');
INSERT INTO `ctripairportname` VALUES ('61', 'guanghan');
INSERT INTO `ctripairportname` VALUES ('62', 'maqin');
INSERT INTO `ctripairportname` VALUES ('63', 'geermu');
INSERT INTO `ctripairportname` VALUES ('64', 'panlong');
INSERT INTO `ctripairportname` VALUES ('65', 'liupanshan');
INSERT INTO `ctripairportname` VALUES ('66', 'tunxi');
INSERT INTO `ctripairportname` VALUES ('67', 'meilan');
INSERT INTO `ctripairportname` VALUES ('68', 'jinchengjiang');
INSERT INTO `ctripairportname` VALUES ('69', 'handan');
INSERT INTO `ctripairportname` VALUES ('70', 'heihe');
INSERT INTO `ctripairportname` VALUES ('71', 'baita');
INSERT INTO `ctripairportname` VALUES ('72', 'xinqiao');
INSERT INTO `ctripairportname` VALUES ('73', 'xiaoshan');
INSERT INTO `ctripairportname` VALUES ('74', 'lianshui');
INSERT INTO `ctripairportname` VALUES ('75', 'zhijiang');
INSERT INTO `ctripairportname` VALUES ('76', 'chilajiao');
INSERT INTO `ctripairportname` VALUES ('77', 'dongshan');
INSERT INTO `ctripairportname` VALUES ('78', 'hami');
INSERT INTO `ctripairportname` VALUES ('79', 'haining');
INSERT INTO `ctripairportname` VALUES ('80', 'nanyue');
INSERT INTO `ctripairportname` VALUES ('81', 'taiping');
INSERT INTO `ctripairportname` VALUES ('82', 'hetian');
INSERT INTO `ctripairportname` VALUES ('83', 'hualian');
INSERT INTO `ctripairportname` VALUES ('84', 'pingtan');
INSERT INTO `ctripairportname` VALUES ('85', 'yaoqiang');
INSERT INTO `ctripairportname` VALUES ('86', 'jinzhou');
INSERT INTO `ctripairportname` VALUES ('87', 'chaoshan');
INSERT INTO `ctripairportname` VALUES ('88', 'jiangmen');
INSERT INTO `ctripairportname` VALUES ('89', 'jingdezhen');
INSERT INTO `ctripairportname` VALUES ('90', 'jiagedaqi');
INSERT INTO `ctripairportname` VALUES ('91', 'jiayuguan');
INSERT INTO `ctripairportname` VALUES ('92', 'jinggangshan');
INSERT INTO `ctripairportname` VALUES ('93', 'jinchuan');
INSERT INTO `ctripairportname` VALUES ('94', 'ertaizi');
INSERT INTO `ctripairportname` VALUES ('95', 'lushan');
INSERT INTO `ctripairportname` VALUES ('96', 'dongjiao');
INSERT INTO `ctripairportname` VALUES ('97', 'qufu');
INSERT INTO `ctripairportname` VALUES ('98', 'jinzhouwan');
INSERT INTO `ctripairportname` VALUES ('99', 'xingkaihu');
INSERT INTO `ctripairportname` VALUES ('100', 'jiaxing');
INSERT INTO `ctripairportname` VALUES ('101', 'huanglong');
INSERT INTO `ctripairportname` VALUES ('102', 'guici');
INSERT INTO `ctripairportname` VALUES ('103', 'kangding');
INSERT INTO `ctripairportname` VALUES ('104', 'kashi');
INSERT INTO `ctripairportname` VALUES ('105', 'gaoxiong');
INSERT INTO `ctripairportname` VALUES ('106', 'huangping');
INSERT INTO `ctripairportname` VALUES ('107', 'kanasi');
INSERT INTO `ctripairportname` VALUES ('108', 'changshui');
INSERT INTO `ctripairportname` VALUES ('109', 'shangyi');
INSERT INTO `ctripairportname` VALUES ('110', 'kuerle');
INSERT INTO `ctripairportname` VALUES ('111', 'kelamayi');
INSERT INTO `ctripairportname` VALUES ('112', 'kunshan');
INSERT INTO `ctripairportname` VALUES ('113', 'guanzhishan');
INSERT INTO `ctripairportname` VALUES ('114', 'zhongchuan');
INSERT INTO `ctripairportname` VALUES ('115', 'liangping');
INSERT INTO `ctripairportname` VALUES ('116', 'sanyi');
INSERT INTO `ctripairportname` VALUES ('117', 'libo');
INSERT INTO `ctripairportname` VALUES ('118', 'lvliang');
INSERT INTO `ctripairportname` VALUES ('119', 'lincang');
INSERT INTO `ctripairportname` VALUES ('120', 'yuezhao');
INSERT INTO `ctripairportname` VALUES ('121', 'gongga');
INSERT INTO `ctripairportname` VALUES ('122', 'linxi');
INSERT INTO `ctripairportname` VALUES ('123', 'beijiao');
INSERT INTO `ctripairportname` VALUES ('124', 'baitabu');
INSERT INTO `ctripairportname` VALUES ('125', 'shubuling');
INSERT INTO `ctripairportname` VALUES ('126', 'bailian');
INSERT INTO `ctripairportname` VALUES ('127', 'lantian');
INSERT INTO `ctripairportname` VALUES ('128', 'milin');
INSERT INTO `ctripairportname` VALUES ('129', 'liping');
INSERT INTO `ctripairportname` VALUES ('130', 'xijiao');
INSERT INTO `ctripairportname` VALUES ('131', 'hailang');
INSERT INTO `ctripairportname` VALUES ('132', 'aomen');
INSERT INTO `ctripairportname` VALUES ('133', 'nanjiao');
INSERT INTO `ctripairportname` VALUES ('134', 'meixian');
INSERT INTO `ctripairportname` VALUES ('135', 'magongjichang');
INSERT INTO `ctripairportname` VALUES ('136', 'mohe');
INSERT INTO `ctripairportname` VALUES ('137', 'xingdong');
INSERT INTO `ctripairportname` VALUES ('138', 'changbei');
INSERT INTO `ctripairportname` VALUES ('139', 'gaoping');
INSERT INTO `ctripairportname` VALUES ('140', 'lishe');
INSERT INTO `ctripairportname` VALUES ('141', 'lukou');
INSERT INTO `ctripairportname` VALUES ('142', 'luguhu');
INSERT INTO `ctripairportname` VALUES ('143', 'nalati');
INSERT INTO `ctripairportname` VALUES ('144', 'wuwei');
INSERT INTO `ctripairportname` VALUES ('145', 'jiangying');
INSERT INTO `ctripairportname` VALUES ('146', 'baoanying');
INSERT INTO `ctripairportname` VALUES ('147', 'simao');
INSERT INTO `ctripairportname` VALUES ('148', 'sanjiazi');
INSERT INTO `ctripairportname` VALUES ('149', 'liuting');
INSERT INTO `ctripairportname` VALUES ('150', 'shanhaiguan');
INSERT INTO `ctripairportname` VALUES ('151', 'qiemo');
INSERT INTO `ctripairportname` VALUES ('152', 'qingyang');
INSERT INTO `ctripairportname` VALUES ('153', 'wulingshan');
INSERT INTO `ctripairportname` VALUES ('154', 'jinjiang');
INSERT INTO `ctripairportname` VALUES ('155', 'qianjiang');
INSERT INTO `ctripairportname` VALUES ('156', 'quzhou');
INSERT INTO `ctripairportname` VALUES ('157', 'heping');
INSERT INTO `ctripairportname` VALUES ('158', 'shekou');
INSERT INTO `ctripairportname` VALUES ('159', 'siping');
INSERT INTO `ctripairportname` VALUES ('160', 'pudong');
INSERT INTO `ctripairportname` VALUES ('161', 'hongqiao');
INSERT INTO `ctripairportname` VALUES ('162', 'taoxian');
INSERT INTO `ctripairportname` VALUES ('163', 'huayuan');
INSERT INTO `ctripairportname` VALUES ('164', 'zhengding');
INSERT INTO `ctripairportname` VALUES ('165', 'fenghuang');
INSERT INTO `ctripairportname` VALUES ('166', 'guangfu');
INSERT INTO `ctripairportname` VALUES ('167', 'baoan');
INSERT INTO `ctripairportname` VALUES ('168', 'hongping');
INSERT INTO `ctripairportname` VALUES ('169', 'tongliao');
INSERT INTO `ctripairportname` VALUES ('170', 'maijishan');
INSERT INTO `ctripairportname` VALUES ('171', 'jiaohe');
INSERT INTO `ctripairportname` VALUES ('172', 'tianmen');
INSERT INTO `ctripairportname` VALUES ('173', 'sanyuanpu');
INSERT INTO `ctripairportname` VALUES ('174', 'taoyuan');
INSERT INTO `ctripairportname` VALUES ('175', 'songshan');
INSERT INTO `ctripairportname` VALUES ('176', 'binhai');
INSERT INTO `ctripairportname` VALUES ('177', 'taidong');
INSERT INTO `ctripairportname` VALUES ('178', 'sannvhe');
INSERT INTO `ctripairportname` VALUES ('179', 'tongxiang');
INSERT INTO `ctripairportname` VALUES ('180', 'wusu');
INSERT INTO `ctripairportname` VALUES ('181', 'tacheng');
INSERT INTO `ctripairportname` VALUES ('182', 'tuofeng');
INSERT INTO `ctripairportname` VALUES ('183', 'qingquangang');
INSERT INTO `ctripairportname` VALUES ('184', 'luqiao');
INSERT INTO `ctripairportname` VALUES ('185', 'diwobao');
INSERT INTO `ctripairportname` VALUES ('186', 'wenchang');
INSERT INTO `ctripairportname` VALUES ('187', 'weifang');
INSERT INTO `ctripairportname` VALUES ('188', 'dashuibo');
INSERT INTO `ctripairportname` VALUES ('189', 'wenshanpuzhehei');
INSERT INTO `ctripairportname` VALUES ('190', 'longwan');
INSERT INTO `ctripairportname` VALUES ('191', 'wuhai');
INSERT INTO `ctripairportname` VALUES ('192', 'tianhe');
INSERT INTO `ctripairportname` VALUES ('193', 'wuyishan');
INSERT INTO `ctripairportname` VALUES ('194', 'sunanshuofang');
INSERT INTO `ctripairportname` VALUES ('195', 'changzhoudao');
INSERT INTO `ctripairportname` VALUES ('196', 'wanning');
INSERT INTO `ctripairportname` VALUES ('197', 'wuqiao');
INSERT INTO `ctripairportname` VALUES ('198', 'wulanhaote');
INSERT INTO `ctripairportname` VALUES ('199', 'liuji');
INSERT INTO `ctripairportname` VALUES ('200', 'qingshan');
INSERT INTO `ctripairportname` VALUES ('201', 'xilinhaote');
INSERT INTO `ctripairportname` VALUES ('202', 'xianyang');
INSERT INTO `ctripairportname` VALUES ('203', 'gaoqi');
INSERT INTO `ctripairportname` VALUES ('204', 'caojiabao');
INSERT INTO `ctripairportname` VALUES ('205', 'dalian');
INSERT INTO `ctripairportname` VALUES ('206', 'guanyin');
INSERT INTO `ctripairportname` VALUES ('207', 'xinyang');
INSERT INTO `ctripairportname` VALUES ('208', 'xingyi');
INSERT INTO `ctripairportname` VALUES ('209', 'xiahe');
INSERT INTO `ctripairportname` VALUES ('210', 'gasa');
INSERT INTO `ctripairportname` VALUES ('211', 'yuyang');
INSERT INTO `ctripairportname` VALUES ('212', 'caiba');
INSERT INTO `ctripairportname` VALUES ('213', 'guangong');
INSERT INTO `ctripairportname` VALUES ('214', 'mingyueshan');
INSERT INTO `ctripairportname` VALUES ('215', 'sanxia');
INSERT INTO `ctripairportname` VALUES ('216', 'yining');
INSERT INTO `ctripairportname` VALUES ('217', 'yiwu');
INSERT INTO `ctripairportname` VALUES ('218', 'chaoyangchuang');
INSERT INTO `ctripairportname` VALUES ('219', 'penlai');
INSERT INTO `ctripairportname` VALUES ('220', 'nanyang');
INSERT INTO `ctripairportname` VALUES ('221', 'taizhou');
INSERT INTO `ctripairportname` VALUES ('222', 'yushubatang');
INSERT INTO `ctripairportname` VALUES ('223', 'lindu');
INSERT INTO `ctripairportname` VALUES ('224', 'lingling');
INSERT INTO `ctripairportname` VALUES ('225', 'ershilipu');
INSERT INTO `ctripairportname` VALUES ('226', 'hedong');
INSERT INTO `ctripairportname` VALUES ('227', 'jinwan');
INSERT INTO `ctripairportname` VALUES ('228', 'zhenjiang');
INSERT INTO `ctripairportname` VALUES ('229', 'zunyi');
INSERT INTO `ctripairportname` VALUES ('230', 'ganzhou');
INSERT INTO `ctripairportname` VALUES ('231', 'zhaotong');
INSERT INTO `ctripairportname` VALUES ('232', 'zhongshan');
INSERT INTO `ctripairportname` VALUES ('233', 'zhanjiang');
INSERT INTO `ctripairportname` VALUES ('234', 'xiangshan');
INSERT INTO `ctripairportname` VALUES ('235', 'zhangjiakou');
INSERT INTO `ctripairportname` VALUES ('236', 'chengjisihan');
INSERT INTO `ctripairportname` VALUES ('237', 'xinzheng');
INSERT INTO `ctripairportname` VALUES ('238', 'zhangjiagang');
INSERT INTO `ctripairportname` VALUES ('239', 'hehua');
INSERT INTO `ctripairportname` VALUES ('240', 'putuoshan');
