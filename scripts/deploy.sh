#!/usr/bin/env bash

cd $(dirname "$0")/../src

zip --exclude __pycache__ -r ../package.zip *
aws --profile deployer --region eu-west-1 lambda update-function-code --function-name messenger --zip-file fileb://../package.zip