from aws_cdk import aws_ec2 as ec2
from aws_cdk import core
from aws_cdk_presidio.constant import *

class AwsVpc:

    def __init__(self,stack):
        self.stack=stack

    def CreateVPC(self,cidr):
        vpc=ec2.CfnVPC(self.stack,"myvpc",
                cidr_block=cidr,
                enable_dns_hostnames=None,
                enable_dns_support=None
            )
        core.Tags.of(vpc).add("Name",vpc.node.path)
        return vpc