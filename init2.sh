yum install -y squid
yum install -y httpd
yum install -y lsof
rm -rf /etc/squid/squid.conf
cp squid.conf /etc/squid/squid.conf
squid stop
squid start
systemctl stop tinyproxy.service