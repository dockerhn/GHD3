# Requirements
* OS: Ubuntu 14.04 LTS
* docker
* docker-machine
* docker-compose

## a. Docker
```sh
$curl -sSL https://get.docker.com/ | sh
$sudo usermod -aG docker ubuntu
```
After installation finished, you can verify your work by runing docker without sudo
```sh
$ docker run hello-world
```
## b. Docker Machine
After install Docker on you machine, you need to install Docker Machine. Download the Machine binary to somewhere in your $PATH (in my machine, i choose /usr/local/bin)
```sh
$ sudo curl -L https://github.com/docker/machine/releases/download/v0.4.0/docker-machine_linux-amd64 > /usr/local/bin/docker-machine
$ chmod a+x /usr/local/bin/docker-machine
$ docker-machine -v
```
## c. Docker-compose
We need to install docker-compose
```sh
$sudo curl -L https://github.com/docker/compose/releases/download/VERSION_NUM/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
```
If previous command failed, you can try to use pip instead:
```sh
$sudo pip install -U docker-compose
$sudo chmod a+x /usr/local/bin/docker-compose (Optional, if you use pip method don't need to do this)
```
