[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Email](../Email.md) / Send

[Previous](Get-by-Name.md) | [Next](../Messengers.md)

# Send Email

The request allows sending emails to clients.

## Rest API

Request Format
    
    
    GET /api/email/send?account=configuration&to=email&name=recipient&subject=subject&body=text

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    GET /api/email/send?account=MailServer&to=john.smith@mail.net&name=John&subject=WebAPI&body=hello
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    EMAIL_SEND|ACCOUNT=configuration|TO=email|NAME=recipient|SUBJECT=subject|BODY=text|\r\n

Response Format
    
    
    EMAIL_SEND|RETCODE=code description|\r\n

## Request Parameters

  * account — the name of the mail server configuration, via which the email will be sent. The "[Name](Data-Structure.md)" field is used for the name.
  * to — recipient's email address.
  * name — recipient's name.
  * subject — email subject.
  * body — email body.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

  * All method parameters are required.
  * To be able to send emails, the platform must have pre-configured mail services.


