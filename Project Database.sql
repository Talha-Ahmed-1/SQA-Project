create database if not exists banquet;
create table if not exists banquet.package (
pkg_id int primary key auto_increment,pkg_name varchar(40),theme varchar(40),guest char(20),duration char(20),functions varchar(20),price int);
create table if not exists banquet.admin (
admin_id int primary key auto_increment,
admin_name char(20),
pass char(20));
insert into banquet.admin(admin_name, pass) values ("hello","test123");
create table if not exists banquet.inventory (
item char(20) ,
 quantity int);
insert into banquet.inventory(
item,quantity) values ("Chair",0),("Table",0),("Glass",0),("Plate",0),("Spoon",0),("Fan",0),("Ac",0);
CREATE table if not exists banquet.Staff(
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(40) NOT NULL,
Address VARCHAR(40) NOT NULL,
Working VARCHAR(40) NOT NULL,Salary INT NOT NULL);
CREATE TABLE if not exists banquet.Booking(
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(40) NOT NULL,
    Event VARCHAR(40) NOT NULL,
    Package VARCHAR(40) NOT NULL,
    Booking_Date VARCHAR(40) NOT NULL,
    Ocassion_Date VARCHAR(40) NOT NULL,
    Price INT NOT NULL );
create table if not exists banquet.Customer(
ID int primary key not null auto_increment,
CName varchar(20) not null,
Address varchar(40) not null
,Mobile varchar(20) not null,Email varchar(40) not null);