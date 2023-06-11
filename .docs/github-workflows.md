## GitHub Workflows

### Overview
GitHub Workflows are automated processes that run configurable jobs. In the case of SmartBard, these jobs will deploy AWS resources into the AWS environment.  
These workflows are defined in the [workflows directory](../.github/workflows)  
For each CloudFormation template defined, there are two workflows, one for the test region and one for the prod region. The two workflows are generally identical except for environment parameters and when deployments should be triggered. Test region allows automatic deployment once a push to the GitHub repo is made, which prod region imposes more retrictions. 

### Parts of a Workflow
1. Name - A name user defines for the workflow
2. On - the conditions on which a workflow is triggered
3. Jobs - The jobs that will run when the workflow is triggered. 
    - Jobs contain steps that will run to deploy AWS resources. These steps include configuring AWS credentials (obtaining parameters stored in the GitHub environment to connect to AWS) and using prefined templated provided by AWS to deploy the resources. 