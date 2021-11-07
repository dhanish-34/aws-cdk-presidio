from aws_cdk import core
from aws_cdk import core as cdk
from aws_cdk import aws_iam as iam

class AwsIamRole():

    def __init__(self, stack):
        self.stack=stack

    def CreateRole(self,role_logicalname,service_principal,role_name,description=None,inline_policies=None,managed_policies=None):
        role=iam.Role(self.stack,id=role_logicalname,
                assumed_by=iam.ServicePrincipal(service_principal),
                description=description,
                inline_policies=inline_policies,
                managed_policies=managed_policies,
                role_name=role_name
        )
        return role
