from aws_cdk import core
from aws_cdk import core as cdk
from aws_cdk import aws_ec2 as ec2

class AwsSecurityGroup():

    def __init__(self, stack):
        self.stack=stack

    def CreateSecurityGroup(self,securityGroup_id,vpc,securitygroup_name):
        security_group=ec2.SecurityGroup(self.stack, securityGroup_id,
                vpc=vpc,
                security_group_name=securitygroup_name
        )
        core.Tags.of(security_group).add("Name",security_group.node.path)
        return security_group
