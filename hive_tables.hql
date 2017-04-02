DROP TABLE IF EXISTS titanic_train;

create external table titanic_train (
  id int,
  survived int,
  class int,
  name string,
  sex string,
  age int,
  sibsip int,
  parch int,
  ticket string,
  fare double,
  cabin string,
  embarked string  
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES 
(
"input.regex" = "^([0-9]*),([0-9]*),([0-9]*),\\\"(.*)\\\",(.*),([0-9]*),([0-9]*),([0-9]*),(.*),([0-9\\.]*),(.*),(.*)"
);

LOAD DATA
INPATH '/titanic/train.csv'
OVERWRITE INTO TABLE titanic_train;


DROP TABLE IF EXISTS titanic_test;

create external table titanic_test (
  id int,
  survived int,
  class int,
  name string,
  sex string,
  age int,
  sibsip int,
  parch int,
  ticket string,
  fare double,
  cabin string,
  embarked string  
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
WITH SERDEPROPERTIES 
(
"input.regex" = "^([0-9]*),([0-9]*),([0-9]*),\\\"(.*)\\\",(.*),([0-9]*),([0-9]*),([0-9]*),(.*),([0-9\\.]*),(.*),(.*)"
);

LOAD DATA
INPATH '/titanic/test.csv'
OVERWRITE INTO TABLE titanic_test;
