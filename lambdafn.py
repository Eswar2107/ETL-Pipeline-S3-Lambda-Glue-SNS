import boto3
glue = boto3.client("glue")
def lambda_handler(event, context):
    glue.start_job_run(JobName="export")
    return {"statusCode": 200, "body": "Glue job export started"}
