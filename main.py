import boto3
from boto3.dynamodb.conditions import Key, Attr

if __name__ == '__main__':
	dynamodb = boto3.resource('dynamodb')

	table = dynamodb.Table('Personajes')

	table.put_item(
		Item = {
			'Id': 123,
			'Gender': 'F',
			'Status': 'Alive'
		}
	)

	response = table.query(
		KeyConditionExpression=Key('Id').eq(69)
	)

	print('Response')
	print('Response')
	print(response)
