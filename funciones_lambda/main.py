def dynamodb_events(event, context):

    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                manejar_insert(record)
                
            if record['eventName'] == 'MODIFY':
                manejar_update(record)
    
            if record['eventName'] == 'REMOVE':
                manejar_delete(record)
    except Exception as error:
        print("ERROR"), error
        return error

            
    return 'Ok!'

def manejar_insert(record):
    print("soy un insert")
    print(record)
    
def manejar_update(record):
    print("soy un update")
    print(record)

def manejar_delete(record):
    print("soy un delete")
    print(record)