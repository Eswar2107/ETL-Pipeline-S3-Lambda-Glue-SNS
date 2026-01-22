# ETL-Pipeline-S3-Lambda-Glue-SNS
This project sets up an automated ETL workflow using AWS services.
When a file is uploaded to an S3 bucket, a Lambda function triggers an AWS Glue ETL job.
EventBridge monitors the Glue job execution and sends an email notification through SNS.

✅ Architecture Overview

Flow:

File uploaded to Amazon S3

S3 event trigger invokes AWS Lambda

Lambda starts the AWS Glue job

EventBridge listens for Glue job events (run status)

EventBridge triggers SNS

SNS sends an email notification
