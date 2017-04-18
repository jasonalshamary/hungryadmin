Scheduled Lambda SQS Message Function With Cloudwatch
=====================================================
:date: 2017-04-17
:tags: AWS, Lambda, Cloudwatch, Python

Recently I wanted to created a schdeduled Lambda event that would send a
message to an SQS queue. I ended up using Cloudwatch to trigger a Python based
Lambda event that would make a call to the appropriate queue.

This process was pretty easy to set up and required configuration within
Cloudwatch and Lambda. I was communicating with an existing SQS queue which was
hooked up to a listening service which I won't go into here.

Setting up Lambda first was required to make sure the job could be triggered
from Cloudwatch successfully, as you can't set up the cloudwatch event until
the Lambda function exists.

Lambda Configuration
--------------------

Begin by creating a new Lambda function and pasting the following code into
the code section (or upload it with Apex, whatever you may use) with the
appropriate changes to the `region_name`, `QueueName` primary message attribute
(currently called `service_class`), and `StringValue`:

.. code-block:: python

  import boto3  
  import json
  
  
  def lambda_handler(event, context):
      
    sqs = boto3.resource('sqs', region_name='us-east-1')
    queue = sqs.get_queue_by_name(QueueName='my_queue')
    
    response = queue.send_message(
        MessageBody='{}',
        DelaySeconds=0,
        MessageAttributes={
            'service_class': {
                'StringValue': 'Service::Worker',
                'DataType': 'String'
            }
        }   
    )
  print(response)

Once this code is in place review the configuration section of the Lambda
function to make sure it has the appropriate Runtime, and set the `Handler`
value to `lambda_function.lambda_handler` as we're calling the function
`lambda_handler`. From there either set a role, or choose an existing role.
You should have an existing role set up for lambda if you've used it before
that has the appropriate permissions.

Depending on your configuration you may need to set additional options in the
`Advanced Settings` section, primarily the VPC, Subnets, and Security Groups.
I'm not going to go into those here as every setup is different and it will
rely heavily on how you have your environment configured. Once those steps
are complete your Lambda function is ready to go. I would suggest testing it
to ensure there are no errors and that it is behaving as you expect.

Cloudwatch Configuration
------------------------

Now that the Lambda function is created the Cloudwatch trigger can be created.
This step is relatively straight forward, head over to the Cloudwatch console,
and create a new rule within `Events`. Once on the configuration page you'll
want to select `Schedule` for the event source, and then enter the appropriate
cron expression depending on when you want your function to run. Set your
target to the Lambda function you created, set any additional options you might
need (which you most likely won't since this is a single message) and then save
the rule. From here you can confirm things are working as expected by reviewing
the Cloudwatch logs that are created when the job runs.

That's pretty much it. With this in place you'll have a scheduled Lambda
function running that doesn't rely on a system within your infrastructure.
