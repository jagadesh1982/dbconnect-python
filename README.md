#dbconnect-python
Sample Code for Connecting to mySql , inserting and querying using python code

#Installing my Sql on Centos 7
wget https://repo.mysql.com/mysql80-community-release-el7-1.noarch.rpm \
yum localinstall mysql80-community-release-el7-1.noarch.rpm \
yum repolist enabled | grep "mysql.*-community.*" \
yum install mysql-community-server \
service mysqld start \
service mysqld status \
mysql --version

#get root password : grep 'temporary password' /var/log/mysqld.log
mysql_secure_installation \

#connect : mysql -u root -p
mysql -u root -p \


#Create DB, Tables  and Insert data
CREATE DATABASE books; \
USE books; \
CREATE TABLE authors (id INT, name VARCHAR(20), book_name VARCHAR(20), email VARCHAR(20)); \
SHOW TABLES; \
INSERT INTO authors (id,name,book_name,email) VALUES(1,"Vivek","davinci code","xuz@abc.com"); \

#Python Libraries
easy_install pip \
pip install mysql-connector-python \

#Running my Sql Docker Container
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=Redhat123@ -d mysql \
docker exec -it some-mysql bash \
