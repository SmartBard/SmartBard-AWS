## AWS Resources Deployment

### Overview
This guide is to document the steps to deploy or make changes to the aws resources. The following steps will walk through the process of updating the cloudforamtion templates governing the AWS resources. 

### Steps
1. Make a change in the yaml files corresponding to the AWS resource that needs to be updated. 
2. Save that change and push into GitHub
    - Note: Any pushed into GitHub will automatically start a deployment in the test region, if there is a change detected by the workflows. Prod deployments will be done manually with more restrictions. 
3. Check the status of the workflow in GitHub. 
    - If it is successful, the logs and Cloudformation stack in the AWS console will let you know. 
    - In case of failures, check the corresponding Cloudformation stack. The `Events` and `Resources` tabs will give more details on the cause of the failure. FIx errors accordingly.
4. In the case of prod deployments, once a branch is merged to master, you will be able to run workflows using the the `Run Workflow` button under the corresponding workflow tab.
5. Lastly, check the AWS resource in the AWS console to ensure that the correct change has been applied. 