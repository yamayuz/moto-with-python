import boto3


class OperateEc2Instance:
    def getInstanceId(self):
        ec2 = boto3.client('ec2', region_name='ap-northeast-1')
        # インスタンスIDを取得
        instances = ec2.describe_instances()
        instance_id = [instance['InstanceId'] for r in
                       instances.get('Reservations') for
                       instance in r.get('Instances')]
        return instance_id
