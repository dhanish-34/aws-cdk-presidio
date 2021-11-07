from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk_presidio.Reusable_modules.ec2 import *
from aws_cdk_presidio.constants import *
from aws_cdk_presidio.Reusable_modules.security_group import *
from aws_cdk_presidio.Reusable_modules.role import *

class AwsCdkPresidioStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, account,region,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        SITE=Test
        ec2object=AwsEc2(stack=self)
        sgobject=AwsSecurityGroup(stack=self)
        iamroleobject=AwsIamRole(stack=self)

        myvpc = ec2.Vpc.from_lookup(self, "myvpc", vpc_name=SITE.VPC_NAME)
        linux_security_group=ec2.SecurityGroup.from_lookup(self,"linux_sg",security_group_id=SITE.SECURITY_GROUP)

        #EC2 role creation
        ec2_role_id ="EC2-role"
        ec2_role_service_principal="ec2.amazonaws.com"
        ec2_role_description="IAM Role used by EC2"
        ec2_role_inline_policies=None
        ec2_role_managed_policies=None
        ec2_role_name="ec2-role"
        ec2_role=iamroleobject.CreateRole(ec2_role_id,ec2_role_service_principal,ec2_role_name,ec2_role_description,ec2_role_inline_policies,ec2_role_managed_policies)

        #Ec2 common parameters
        linux_volume_size=SITE.LINUX_VOLUME_SIZE
        linux_image_id=SITE.LINUX_AMI_ID
        linux_instance_type=SITE.LINUX_INSTANCE_TYPE
        linux_key_pair=SITE.EC2_KEY_PAIR

        #linux1 instance creation
        linux1_server_name=SITE.LINUX1_SERVER_NAME
        linux1_instanceprofile_id="linux-instance_profile"
        linux1_ec2=ec2object.CreateServer(linux1_server_name,linux_volume_size,linux_image_id,linux1_instanceprofile_id,ec2_role.role_name,linux_instance_type,linux_key_pair,linux_security_group.security_group_id)

        #linux2 instance creation
        linux2_server_name=SITE.LINUX2_SERVER_NAME
        linux2_instanceprofile_id="linux-instance_profile-b"
        linux2_ec2=ec2object.CreateServer(linux2_server_name,linux_volume_size,linux_image_id,linux2_instanceprofile_id,ec2_role.role_name,linux_instance_type,linux_key_pair,linux_security_group.security_group_id)
