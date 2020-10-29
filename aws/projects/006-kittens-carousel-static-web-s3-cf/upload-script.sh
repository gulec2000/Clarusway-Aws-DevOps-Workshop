#!/bin/bash

cd ~/serdar_cw_workshop/Clarusway-Aws-DevOps-Workshop/aws/projects/006-kittens-carousel-static-web-s3-cf/static-web
aws s3 ls
aws s3 sync . s3://kittens.gulecserdar.de
aws s3 ls s3://kittens.gulecserdar.de