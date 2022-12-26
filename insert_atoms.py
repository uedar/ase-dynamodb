import boto3
import json
import decimal


def create_table(dynamodb=None):
    table = dynamodb.create_table(
        TableName="Atoms",
        KeySchema=[{"AttributeName": "unique_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "unique_id", "AttributeType": "S"}],
        ProvisionedThroughput={"ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    return table


def insert_data(table):
    atoms1 = json.load(open("sample_data.json", "r"), parse_float=decimal.Decimal)["1"]
    atoms_list = [atoms1]

    with table.batch_writer() as batch:
        for atoms in atoms_list:
            batch.put_item(Item=atoms)


if __name__ == "__main__":
    dynamodb = boto3.resource(
        service_name="dynamodb",
        endpoint_url="https://dynamodb.us-west-2.amazonaws.com",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name="us-west-2",
    )
    TABLE_NAME = "prototype1"
    atoms_table = dynamodb.Table(TABLE_NAME)
    print(f"Table status: {atoms_table.table_status}")
    insert_data(atoms_table)
