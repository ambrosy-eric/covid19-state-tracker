import boto3
import json

def send_sns(message):
    arn = 'arn:aws:sns:us-east-1:327019230308:personal_emailer'
    client = boto3.client('sns')
    response = client.publish(
        TargetArn=arn,
        Message=json.dumps({'default': json.dumps(message)}),
        MessageStructure='json'
)