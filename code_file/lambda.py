
import boto3
import base64
import json
from io import StringIO

def normal(result):
    final = [float(item.strip()) for item in result]
    final = [ 'Normal!' if item == 0 else 'Abnormal!' for item in final]
    # if float(final) == 0:
    #     final = 'Normal!'
    # else:
    #     final = 'aaa'
    return final

def lambda_handler(event, context):
    '''
    lambda function is trggered by new data in the Kinesis stream
    '''
    # Create SageMaker runtime client
    sagemaker_runtime = boto3.client('sagemaker-runtime')
    endpoint_name = 'sagemaker-xgboost-2023-12-05-16-52-41-391'
    
    # print('Processing event: %s', str(event)) 
    
    payload = []
    
    # Read Kinesis stream data records
    for record in event['Records']:
        #Kinesis data is base64 encoded so decode here
        data = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        
        if data:
            print(data)
            response = sagemaker_runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='text/csv',
            Body=data)
            
            result = response['Body'].read().decode('ascii')
            
            payload.append(result)


    # Invoke the SageMaker endpoint using the Kinesis stream data
    if payload:
        payload = normal(payload)
        pred = ['pred_'+str(i) for i in range(len(payload))]
        
        print(payload[0])
        
        return {'statusCode' : 200, 'prediction' : payload[0]}

    # else:
    #     # return nothing if no records were processed
    #     # inference_result = {'predictions':[]}
    #     # print(f'No kinesis records to process: {inference_result}')
    #     print('No data')
    #     return {'statusCode': 200, 'body': json.dumps('No data')}

