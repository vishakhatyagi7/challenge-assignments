# Challenge - 1

Pre-requisites:
- Terraform
- aws-cli
- an AWS with its access credetial keys

Pre-requisites on AWS:
- A key to ssh into the servers
- Bastion host

All the commands are to be run from the folder "Challenge-1/main".
A sample ".tfvar" is present for usage which expects a key names "myDMZ" to be present in the AWS environment.

Run the following commands to deploy this infrastructure:
1. terraform init
2. terraform workspace new sit (optional)
3. terraform plan -var-file="sit.tfvar" 
4. terraform apply -var-file="sit.tfvar"


This should launch a basic 3-tier infra includig a VPC, private and public subnets, an internet-facing ALB, an autoscaling group of Ec2 instances in private subnets, an RDS cluster in private subnets, and all under underlying minor resources.
