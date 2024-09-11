import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    # Fetch the instance ID and action from the event input
    instance_id = event.get('instance_id')  # Instance ID should come from the event
    action = event.get('action')  # Action should come from the event ('start' or 'stop')

    if not instance_id or action not in ['start', 'stop']:
        return {
            'statusCode': 400,
            'body': 'Invalid input. Provide instance_id and action ("start" or "stop").'
        }

    try:
        if action == 'start':
            # Start the EC2 instance
            response = ec2.start_instances(InstanceIds=[instance_id])
            return {
                'statusCode': 200,
                'body': f'Starting instance {instance_id}.'
            }

        elif action == 'stop':
            # Stop the EC2 instance
            response = ec2.stop_instances(InstanceIds=[instance_id])
            return {
                'statusCode': 200,
                'body': f'Stopping instance {instance_id}.'
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
