# Severless Data Pipeline in AWS
![codebuild-badge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiYkJVbFdhMUhtRFRTY3J4L3FodkRJQzVHSEU0V1JMUW1oRDVTa3RXSStjOTI5WXdkRFdnbWJMNzUzMVQrZWV0UDcrU3BiSFd6OGF3dWRUT2VUcWtaU2FrPSIsIml2UGFyYW1ldGVyU3BlYyI6Ik56WFZnQ1NLbEluMHVpMnoiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

This project aims to automate the process of collecting tweets from Twitter in a regular basis and store data in S3 bucket. Right now, this project is scheduled to collect Downald Trump's most recent tweets every 6 hour, perform sentiment analysis using AWS Comprehend on his tweets and save into S3 bucket.

## Motivation
I want to build a data pipeline to automate the process of data collection in real time. The data pipeline should be able to collect and store data from any source given valid API and access previliage(Twitter, Wikipedia and, etc.). And I, as a user, can easily change the frequency of data scrapping.

## Features
- 100% built and deployed on AWS
- Serverless Data Pipeline built with Lambda, SQS, DynamoDB and S3
- Utilized AWS machine learning service Comprehend
- CI+CD(To be finished)

## Screenshots
Producer Lambda Function Design Graph:
![producer](./resources/producer.png)
Consumer Lambd Function Design Graph: 
![consumer](./resources/consumer.png)
## Framework
Data Pipelien Diagram:
![diagram](./resources/data-pipeline.png)
Interested in my web app? https://github.com/wensu425/aws-eb-webapp.git
