#/!bin/bash

now=`date '+%Y-%m-%d %H:%M:%S'`
echo $now [Install yum-utils for yum-config-manager]
#yum install -y yum-utils
echo $now [add repository]
#yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
echo $now [VERIFY KEY FINGERPRINT]
#yum makecache fast
echo $now [INSTALL DOCKER]
#yum install -y docker-ce
#yum install docker-ee
echo $now [START DOCKER]
#systemctl start docker
echo $now [TEST DOCKER]
docker run hello-world
