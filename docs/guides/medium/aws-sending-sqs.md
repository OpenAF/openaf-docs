---
layout: default
title: Sending AWS SQS messages
parent: Medium
grand_parent: Guides
---

# Sending AWS SQS messages

AWS provides a simple message queueing service called [AWS SQS](https://aws.amazon.com/sqs/). Compared with many other message queueing services it's simple, scalable and, above all, cheap. It's provides simple queues and FIFO queues. The message visibility feature allows for any process (including an OpenAF script) to retrieve a message and if it fails to process it, after a specific timeout, AWS SQS will assume it failed and will place the message back in queue.

## Sending messags

The functionality is available with the AWS opack. To install it simple execute:

````javascript
opack install AWS
````

> You can also retrieve the opack file from https://openaf.io/opack/AWS.opack and install it using ````opack install AWS.opack````

Now you will need to login into AWS API either using a provided id & secret OR letting it try to retrieve from other AWS authentication methods (like AWS IAM role, for example):

````javascript
loadLib("aws.js")
var aws = new AWS("myId", "mySecret")   // or simply: var aws = new AWS()
````

### Simple queue

To send a message to a simple queue you will need to know:

* the SQS specific queue endpoint URL (this can be found on the AWS SQS portal)
* the SQS queue region (e.g. us-east-1)

Now simply execute:

````javascript
aws.SQS_Send("123456789012/test", "us-east-1", "This is my first message")
````

Depending on your use case it might be more useful to send a json string:

````javascript
aws.SQS_Send("123456789012/test", "us-east-1", stringify(myData, __, ""))
````

### FIFO queue

Sending messages to a FIFO queue differs from the simple queue by adding:

* a message group ID
* a message deduplication ID

So now the code would look like this:

````javascript
var msg = "My first FIFO message"
var groupId = "topic1"
var msgDedupId = genUUID()
aws.SQS_Send("123456789012/test.fifo", "eu-west-1", msg, groupId, msgDedupId)
````

And that's it. That's all it takes to send a SQS message in OpenAF.

> You can send more than one message per call (up to 10 by AWS limitations). Check how to send an array of messages by executing ````help AWS.SQS_Send```` on an OpenAF console

## Receiving messages

To receive the messages in queue you can use the _SQS_Receive_ and _SQS_Delete_ functions.

````javascript
loadLib("aws.js")

// Connect to AWS API
var aws = new AWS()

// You can find this on the SQS queue info
var sqsEndpointURI = "123456789012/test"
var sqsRegion      = "us-east-1"

var recv
do {
  print("Waiting for a message...")
  // Wait for 5 seconds for a message. If a message is received it will promise to handle it in 10 seconds (otherwise it will go back to SQS automatically)
  recv = aws.SQS_Receive(sqsEndpointURI, sqsRegion, 10, 5)

  if (isMap(recv) && isDef(recv.ReceiveMessageResponse) && isMap(recv.ReceiveMessageResponse.ReceiveMessageResult)) {
     // we have received a message
     var msg = recv.ReceiveMessageResponse.ReceiveMessageResult.Message

     // If the body is a JSON message it can be parsed to be used in OpenAF
     //var msgJson = jsonParse(msg.Body)
     tprint("..received: {% raw %}{{MessageId}}{% endraw %} | {% raw %}{{{Body}}}{% endraw %}", msg)
     // ok, now we have to delete it to ack that was correctly processed
     aws.SQS_Delete(sqsEndpointURI, sqsRegion, msg.ReceiptHandle)
  }
} while(1)
````

You can check more details by executing, on an OpenAF console:

* ````help AWS.SQS_Send````
* ````help AWS.SQS_Receive````
* ````help AWS.SQS_Delete````
* ````help AWS.SQS_MessageVisibility```` (because you might need to extend the time to process a message)
* ````help AWS.SQS_GetQueueAttributes````
* ````help AWS.SQS_Purge````
