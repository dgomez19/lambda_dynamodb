import boto3
from boto3.dynamodb.conditions import Key, Attr

print("HOLA MUNDO")
print("HOLA MUNDO")
print("HOLA MUNDO", __name__)

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Personajes')

response = table.query(
    KeyConditionExpression=Key('Id').eq(69)
)

print('Response')
print('Response')
print(response)
