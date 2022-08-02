import boto3
from moto import mock_ec2
from src.OperateEc2Instance import OperateEc2Instance


class TestPrintEc2InstanceId:
    @mock_ec2
    def test_print_instance_id(self):
        ec2 = boto3.client('ec2', region_name='ap-northeast-1')
        ec2.run_instances(
            ImageId='xxxxx',
            MinCount=1,
            MaxCount=1,
            KeyName="ec2-1",
            TagSpecifications=[{'ResourceType': 'instance',
                                'Tags': [{'Key': 'Name', 'Value': 'ec2-1'}]}])

        app_ins = OperateEc2Instance()
        assert app_ins.getInstanceId() != ''
