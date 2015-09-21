# [T3kpTun](https://github.com/dockerhn/GHD3/) ![T3kpTun Status](https://github.com/dockerhn/GHD3/blob/master/resources/VersionStatus.svg "Version Status")
###A simple way for dockerizing your applications

![Dockerhanoi Tool](resources/Idea_definition.png "T3kpTun definition")

## What is it?

* Starting from your github repository, t3kpTun trys to generate Dockerfile describing how to package your source code application. We define the input form in which you could figure out various parameters for the application including webserver (Apache or Tomcat), dependencies, TCP ports, linked services, etc. 
* t3kpTun supports Dockerfile and Docker compose editor directly from browser so that you could find easily to review and update these generated files if needed.
* Then, t3kpTun helps to deploy these bundle of your audited files and source code into pre-deployed Swarm cluster under your AWS account.
* t3kpTun automatically saves both of Dockerfile and Docker compose file for versioning and re-using purpose.
* t3kpTun supports historical view on your past deployments and building log. You could easily copy a previous deployment by one-click.

##Targeted User

Developers or Technical staffs:
* Want to run their source code (Github) with Docker native technologies on Public Cloud (AWS, Azure,..) or Private Cloud (Openstack, Vmware vCloud,...)
* Have the source code (Github) but don't have or have a little knowledges about Docker before.
* Look for a simplest way to deploy app on Docker with best practice from Docker Experts

##Architecture

##Requirements

1. [Amazon Web Service Account](https://aws.amazon.com/) 
2. [GitHub Account](https://github.com/) 
3. Internet :)

##Getting started
Dockerize your App and Automatic Deployment with T3kpTun

http://ec2-52-74-0-120.ap-southeast-1.compute.amazonaws.com/

##Demo

##Local Installation and documentation

##Next Version

##Authors

1. Nguyen Sy Thanh Son (https://github.com/thanhson1085)
2. Tran Huu Cuong (https://github.com/tranhuucuong91)
3. thaivq7985 (https://github.com/thaivq7985)

T3kpTun is a SaaS, however, you can install locally on your PC

## License - MIT

The T3kpTun code is licensed under the MIT license.

T3kpTun: Copyright (c) 2015 Docker-Ha Noi. http://www.meetup.com/docker-hanoi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
