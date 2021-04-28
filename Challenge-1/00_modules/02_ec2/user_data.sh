#!/bin/bash
sudo yum update -y
sudo yum install -y httpd
echo "Welcome to the JungleBook" > /var/www/html/index.html
curl http://169.254.169.254/latest/meta-data/local-hostname > /var/www/html/index.html
sudo systemctl start httpd
sudo systemctl enable httpd
