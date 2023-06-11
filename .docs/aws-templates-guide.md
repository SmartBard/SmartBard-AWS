## AWS Templates Guide

### Overview
All the AWS resources are managed through CloudFormation templates location in the [cfn-stacks directory](../cfn-stacks). 

Here are the main components of the template:
 - Parameters - Input values, such as environment suffixes for resource name, passed into the template
 - Resources - AWS resource(s) defined and their respective settings
 - Output - Values from the resources that can be exported  

These templates are then deployed into AWS through github workflows. (Read more on github deployments in the other guide - [aws-resources-deployment.md](./aws-resources-deployment.md))  

Below is a brief description of all the services employed in the SmartBard Project. To learn more about the AWS services, please reference the AWS Developer Guides.  

### CloudFront
Template Location: [cloudfront.yaml](../cfn-stacks/cloudfront.yaml)    
Workflow Location: 
 - [deploy-cloudfront.yml](../.github/workflows/deploy-cloudfront.yml)
 - [prod-deploy-cloudfront.yml](../.github/workflows/prod-deploy-cloudfront.yml)

Info:  

The resources contained in the template set up AWS Cloudfront which is the content distribution service that allows traffic through the application. 

### Cognito
Template Location: [cognito.yaml](../cfn-stacks/cognito.yaml)  
Workflow Location: 
 - [deploy-cognito.yml](../.github/workflows/deploy-cognito.yml)
 - [prod-deploy-cognito.yml](../.github/workflows/prod-deploy-cognito.yml)  

Info:  
The resources contained in this template manage user access to the application. The user pool handles login and signup of users and provides tokens to be used in the duration of a user's session. Additionally, the template contains a lambda that handles blocking users that do not have an obs google email from login/signup.  

### RDS
Template Location: [db.yaml](../cfn-stacks/db.yaml)  
Workflow Location: 
 - [deploy-db.yml](../.github/workflows/deploy-db.yml)
 - [prod-deploy-db.yml](../.github/workflows/prod-deploy-db.yml)  

 Info:  
 The resources in the template define the database for the application that stores user and announcement data. More information on the database design can be found in the SRS and Design Document.  

### EC2
Template Location: [ec2.yaml](../cfn-stacks/ec2.yaml)  
Workflow Location: 
 - [deploy-ec2.yml](../.github/workflows/deploy-ec2.yml)
 - [prod-deploy-ec2.yml](../.github/workflows/prod-deploy-ec2.yml)  

 Info:  
 The resources in this template define the virtual server on which the application runs. This includes the load balancer and target group that receive and forward HTTPS requests from the SmartBard API. 

### IAM
Template Location: [iam.yaml](../cfn-stacks/iam.yaml)  
Workflow Location: 
 - [deploy-iam.yml](../.github/workflows/deploy-iam.yml)
 - [prod-deploy-iam.yml](../.github/workflows/prod-deploy-iam.yml)  

 Info:  
 The reources defined in this template manage the permissions/access the users/resources are allowed to have in the form of roles and users. 

### S3
Template Location: [s3.yaml](../cfn-stacks/s3.yaml)  
Workflow Location: 
 - [deploy-s3.yml](../.github/workflows/deploy-s3.yml)
 - [prod-deploy-s3.yml](../.github/workflows/prod-deploy-s3.yml)  

 Info:  
 The resources in this template define the bucketa and access points in which annoucement data, such as image attachments, are stored.

### VPC
Template Location: [vpc.yaml](../cfn-stacks/vpc.yaml)  
Workflow Location: 
 - [deploy-vpc.yml](../.github/workflows/deploy-vpc.yml)
 - [prod-deploy-vpc.yml](../.github/workflows/prod-deploy-vpc.yml)  

 Info:  
 The resources in this template define the private cloud computing environment in which all our previously mentioned resources are contained. 
