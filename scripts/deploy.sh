#!/usr/bin/env bash


cd $(dirname "$0")/..

rm package.zip
rm -rf package
pip install --platform manylinux2014_aarch64 --target=package --implementation cp --python-version 3.12 --only-binary=:all: --upgrade .
cd package
zip -r ../package.zip . --exclude "**/__pycache__/*" --exclude "__pycache__/*"
cd ../src

zip  ../package.zip handler.py --update
aws --profile deployer --region eu-west-1 lambda update-function-code --function-name messenger --zip-file fileb://../package.zip