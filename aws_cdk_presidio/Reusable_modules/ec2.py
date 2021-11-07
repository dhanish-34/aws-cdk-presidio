from aws_cdk import core
from aws_cdk import core as cdk
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam

class AwsEc2():

    def __init__(self, stack):
        self.stack=stack

    def CreateServer(self,ec2_server_name,volume_size,image_id,instanceprofile_id,role_name,instance_type,key_pair,security_group):
        ec2_server = ec2.CfnInstance(self.stack,
            id=ec2_server_name,
            block_device_mappings=[
                ec2.CfnInstance.BlockDeviceMappingProperty(
                    device_name="/dev/sda1",
                    ebs=ec2.CfnInstance.EbsProperty(
                        delete_on_termination=False, encrypted=True, volume_size=volume_size
                    ),
                )
            ],
            ebs_optimized=True,
            disable_api_termination=True,
            image_id=image_id,
            iam_instance_profile=iam.CfnInstanceProfile(
                        self.stack,
                        id=instanceprofile_id,
                        roles=[role_name]
                    ).ref,
            instance_type=instance_type,
            key_name=key_pair,
            security_group_ids=[security_group],
        )
        core.Tags.of(ec2_server).add("Name", ec2_server.node.path)
        return ec2_server
