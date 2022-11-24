#!/bin/bash
yum update -y
yum install -y epel-release
# yum install -y tinyproxy
yum install -y wget git
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
yum install libffi-devel -y
systemctl stop firewalld.service
yum install -y squid
yum install -y httpd
yum install -y lsof
rm -rf /etc/squid/squid.conf
cp squid.conf /etc/squid/squid.conf
squid stop
squid start
# sed -i "s/Allow 127.0.0.1/#Allow 127.0.0.1/g" /etc/tinyproxy/tinyproxy.conf
# service tinyproxy restart
cd ~
wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tar.xz
tar -xvJf  Python-3.7.5.tar.xz
mkdir /usr/local/python3
cd Python-3.7.5
./configure --prefix=/usr/local/python3
make && make install
ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3.7
ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3.7
pip3.7 install redis tornado requests environs

# systemctl stop tinyproxy.service
python3.7 -V
pip3.7 -V