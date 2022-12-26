import boto3
from boto3.dynamodb.conditions import Key, Attr
import os

class DB:
    def __init__(
        self,
        service_name="dynamodb",
        endpoint_url='http://localhost:8000',
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="",
        table_name=""
    ):
        self.resource = boto3.resource(
            service_name=service_name, 
            endpoint_url=endpoint_url,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )
        self.table = self.resource.Table(table_name)


    def get(self):
        options = {
            "IndexName": "calculator-index",
            "KeyConditionExpression": Key("calculator").eq("state"),
            "FilterExpression": Attr("key_value_pairs.functional").eq("ggapbe"),
        }
        response = self.table.query(**options)
        print(response["Items"])
        return response["Items"]


    def update(atoms):

