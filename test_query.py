import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(
    service_name="dynamodb",
    endpoint_url="https://dynamodb.us-west-2.amazonaws.com",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name="us-west-2",
)
TABLE_NAME = "prototype1"
table = dynamodb.Table(TABLE_NAME)

options = {
    "IndexName": "calculator-index",
    "KeyConditionExpression": Key("calculator").eq("state"),
    "FilterExpression": Attr("key_value_pairs.functional").eq("ggapbe"),
}
response = table.query(**options)
print(response["Items"])
