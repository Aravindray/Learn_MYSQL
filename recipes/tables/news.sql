# news.sql

DROP TABLE IF EXISTS news;
#@ _CREATE_TABLE_
CREATE TABLE news
(
  id      INT UNSIGNED NOT NULL AUTO_INCREMENT,
  article BLOB,
  PRIMARY KEY (id)
);
#@ _CREATE_TABLE_
