#!/usr/bin/env bash


cd $(dirname "$0")/..

rm -rf package
rm package.zip
zip -r package.zip images
pip install --platform manylinux2014_x86_64 --target=package --implementation cp --python-version 3.12 --only-binary=:all: --upgrade .
cd package
zip -r ../package.zip . --exclude "**/__pycache__/*" --exclude "__pycache__/*"
cd ../src

zip  ../package.zip handler.py --update
# aws --profile deployer --region eu-west-1 lambda update-function-code --function-name clock --zip-file fileb://../package.zip
rm -rf ../package
