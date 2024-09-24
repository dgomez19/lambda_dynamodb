# dynamodb
python3 -m venv dynamodb
source dynamodb/bin/activate
python3 -m pip install awscli
aws configure
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
pip install boto3

 aws help | grep dynamodb

 aws dynamodb help

 # Listar tablas creadas en DynamoDB:
 aws dynamodb list-tables

 # Crear una tabla
 aws dynamodb wizard new-table

 # Eliminar una tabla
aws dynamodb delete-table --table-name "nomnbre_tabla"


aws dynamodb batch-write-item --request-items file:///Users/dgomez/dev/estudio_daniel/dynamodb/songs.json

# Crear rol
aws iam create-role --role-name dynamodbStreamsRole --assume-role-policy-document file:///Users/dgomez/dev/estudio_daniel/dynamodb/funciones_lambda/role.json

# Crear policy
aws iam put-role-policy --role-name dynamodbStreamsRole --policy-name lambdapermissions --policy-document file:///Users/dgomez/dev/estudio_daniel/dynamodb/funciones_lambda/policy.json

# Convertir archivo a .zip
zip function.zip main.py 

# Crear función lambda, subirla a aws:
aws lambda create-function --function-name lambda-export --role arn:aws:iam::992382733156:role/dynamodbStreamsRole --runtime python3.9 --handler main.dynamodb_events --publish --zip-file fileb:///Users/dgomez/dev/estudio_daniel/dynamodb/funciones_lambda/function.zip