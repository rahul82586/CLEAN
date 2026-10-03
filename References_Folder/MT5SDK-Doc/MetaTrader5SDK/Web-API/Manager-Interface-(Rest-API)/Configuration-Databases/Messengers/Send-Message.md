[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Messengers](../Messengers.md) / Send Message

[Previous](Get-by-Name.md) | [Next](../Gateways.md)

# Send Message

The request allows sending SMS messages to clients.

## Rest API

Request Format
    
    
    GET /api/messenger/send?to=phone&from=sender&group=group&text=message

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/messenger/send?to=+1227122999&from=abcbroker&group=demoforex&text=hello
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    MESSENGER_SEND|TO=phone|FROM=sender|GROUP=group|TEXT=message|\r\n

Response Format
    
    
    MESSENGER_SEND|RETCODE=code description|\r\n

## Request Parameters

  * to — recipient's phone number in the format of +[country code][number], example: +15415553594. The number is indicated without spaces.
  * from — message sender name. It is only used if the appropriate function is supported by the provider. The parameter is optional.
  * group — the parameter can be used to specify the group to which the message recipient's account belongs. In this case, the platform will send the message using the first provider, who holds the settings of the specified group. The parameter is optional: if it is not specified, the provider will be selected without regard to the group.
  * text — message text. The maximum allowable length depends on the provider.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * To be able to send emails, the platform must have pre-configured messengers.
  * Response code [14000](../../../../Return-Codes/Messengers.md) means that the specified phone number is invalid.
  * Response code [14001](../../../../Return-Codes/Messengers.md) means that a landline phone number is specified instead of a mobile phone number.


