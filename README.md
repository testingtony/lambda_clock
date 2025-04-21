AWS Lamba Clock
===============

A lambda function that can be called from a URL. It returns a bitmap suitable for the flipdot-clock.


Update Function Code
--------------------

Run the script `scripts/build.sh`

Run `aws --profile deployer --region eu-west-1 lambda update-function-code --function-name clock --zip-file fileb://package.zip`


Create the Lambda
-----------------

Install aws sam cli https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html

Run the commands `sam build` and `sam deploy`
