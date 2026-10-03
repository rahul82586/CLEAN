[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Mail](../Mail.md) / Send

[Previous](Data-Structure.md) | [Next](Get-Without-Body.md)

# Sending an Email

This request is used for sending emails via the internal mailing system of the trading platform.

## Rest API

Request format
    
    
    POST /api/mail/send?to=login&subject=subject&from_name=name
    { email text }

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    POST /api/mail/send?to=764636&subject=Welcome&from_name=John%20Smith
    \<html\>\<body\>Welcome to MetaTrader 5\<\/body\>\<\/html\>
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    MAIL_SEND|TO=login|SUBJECT=subject|FROM_NAME=name|\r\n
    { email text }

Response format
    
    
    MAIL_SEND|RETCODE=code description|\r\n

## Request Parameters

  * to — the login of the email recipient. You may use the mask "*" as well as specify login ranges in this parameter. Example:


  * to=* — the email will be sent to all clients
  * to=demo*,preliminary — the email will be sent to all clients from groups "demo" and "preliminary".
  * to=100-250,5000-7500 — the email will be sent to all clients from groups "demo" and "preliminary".
  * subject — email subject.
  * from_name — the name of the email sender. Optional parameter.



The email body is passed as an additional body of the request command in the Unicode format. You may use HTML to format emails. The body length must be no more than 8192 characters (16 KB).

> Emails are sent only to the accounts which are available to the manager account used for Web API [connection](../Text-Protocol-(Raw-API)/Authentication.md#client-start) the to the trade server. Available client groups are defined by the "Groups" parameter in the [manager account settings (#manager-configuration)](../../Getting-Started.md#manager-configuration).

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.


