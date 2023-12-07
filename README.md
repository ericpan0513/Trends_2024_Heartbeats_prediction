# Trends_2024_Heartbeats_prediction
## Project Overview
Even though the healthcare industry generates huge volumes of data on a daily basis that can be utilized in many ways to improve the healthcare industry, it fails to fully utilize it due to issues with its usability. Yet there are a significant number of areas where the healthcare industry is continuously utilizing big data.

The main area in which the healthcare industry is actively leveraging big data is to improve hospital administration so that patients can revoke best-in-class clinical support. Apart from that, big data is also used to fight lethal diseases like cancer. Big Data has also helped the industry 
save itself from potential frauds and the usual man-made errors like providing the wrong dosage, medicine, etc. 

Our project focuses on processing heart rate analysis to make more accurate predictions and detect health problems early. This is a real-time prediction system for heart rate that uses machine learning and stream processing platforms. This system helps medical care providers and patients avoid heart rate risk in real time.

Our solution broadly consists of the following sections:  
**(1) Streaming data source and ingestion**:  
We use Amazon Kinesis Data Streams to make data available for further processing.  
  
**(2) Model training and deployment**:   
We use the Heartbeat Categorization dataset from the Kaggle Data Repository to train an ML model-based algorithm using SageMaker. The pre-trained model is stored and used as the designated endpoint for making predictions.  

**(3) Prediction**:   
We use AWS Lambda to connect Kinesis and SageMaker. Lambda takes in input data, invokes the pre-trained model endpoint, and generates predictions.
Result Monitoring: Leveraging AWS CloudWatch, we construct a user-friendly, real-time dashboard to monitor the outcomes of predictions.  

![WhatsApp Image 2023-12-04 at 23 13 30_73641610](https://github.com/ericpan0513/Trends_2024_Heartbeats_prediction/assets/67946408/6fabed61-8abe-42be-8fe6-ab99ff271c8d)  


Our project has a wide range of applications in various industries. Some of the industries are health care, sports, fitness, insurance, and many more. These insights can be used to improve products and services, reduce costs, and increase revenue.

## Dataset
We are using the MIT-BIH Arrhythmia Dataset:   
https://www.kaggle.com/datasets/shayanfazeli/heartbeat/data

# Getting Started
## Setup instruction
Using the code file in this repository, the following gives the instruction on how to set up the project based on AWS.  

### Sagemaker
Set up Sagemaker, train the model and deploy the model:
1. Navigate to Sagemaker Console, and initiated a notebook instance.
2. Open Jupyter Lab, upload `sagemaker.ipynb` and `mitbih_train`.
3. Open `sagemaker.ipynb` on Jupyter Lab, run all.
After the training process and model deploy, we now get the model endpoint that can be accessed by Lambda and Kinesis.

### Kinesis
Set up Kinesis data stream:  
1. Go to the Kinesis console. Select Kinesis Data Streams and click Create data stream.
2. Name the data stream as "input-stream" or any preferred name of your choice. Make sure to recall this data stream name for future data ingestion. Once you've configured the data stream capacity and clicked "Create data stream," Kinesis is now ready to go.
3. Launch your preferred IDE. Open `stream_writer.py` file and input your `aws_access_key_id, aws_secret_access_key, aws_region` and `stream_name`. The stream_name should correspond to the Kinesis data stream name we created earlier.
4. Set `csv_file_path` to the path of `mitbih_test.csv`
5. Execute the "stream_writer.py" file, and after a few minutes of latency, the data should be sent to Kinesis.
<img width="821" alt="Screenshot 2023-12-06 175710" src="https://github.com/ericpan0513/Trends_2024_Heartbeats_prediction/assets/67946408/567bb82e-9d46-4300-9f75-af23487994fb">  


### Lambda
1. Navigate to the Lambda console, create a new function, and select "Author from scratch." Keep the default settings for the remaining configurations.
2. Copy and paste the `lambda.py` code into the Lambda function's code source, input the model endpoint name, and deploy the function.  

 <img width="603" alt="Screenshot 2023-12-06 175857" src="https://github.com/ericpan0513/Trends_2024_Heartbeats_prediction/assets/67946408/e9ef7918-74a1-4a6c-ac16-02e3fa1472a0">     

3. Click `Add trigger` and configure Kinesis as a trigger. This setup will ensure that the Lambda function is triggered, allowing it to generate prediction results when data is received from the Kinesis stream.
<img width="594" alt="Screenshot 2023-12-06 180042" src="https://github.com/ericpan0513/Trends_2024_Heartbeats_prediction/assets/67946408/18b42dc1-7136-48b6-9bcf-813c305e53ec">  

### CloudWatch
After setting up Sagemaker, Kinesis and Lambda, we can navigate to AWS CloudWatch to see the output result.
1. Navigate to CloudWatch
2. Click `Logs -> Log groups` on left Menu.
3. Click on the log group named `lambda-handler`
4. Find the current running log streams, then you can see the streaming output.  
<img width="984" alt="Screenshot 2023-12-06 180549" src="https://github.com/ericpan0513/Trends_2024_Heartbeats_prediction/assets/67946408/2c1870fc-aa91-42ef-9b0e-650ccf6e88a6">

## Project Deliveries
#### Project Video
Here's the youtube link for our presentation:  
https://www.youtube.com/watch?v=fpeDhbenfug 
#### Project Flyer
See `flyer.pdf`

## Reference
1. https://medium.com/@lukekerbs/real-time-anomaly-detection-with-aws-sagemaker-kinesis-streams-214173b0b0e1
2. https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html
