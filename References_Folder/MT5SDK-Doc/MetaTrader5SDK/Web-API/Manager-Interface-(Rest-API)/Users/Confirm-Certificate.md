[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Confirm Certificate

[Previous](Delete-Certificate.md) | [Next](Get-OTP-Key.md)

# Confirm user certificate

This request enables the confirmation of a user certificate if such a confirmation is required by the relevant group settings.

## Rest API

Request Format
    
    
    GET /api/user/certificate/confirm?login=login
    POST /api/user/certificate/confirm?login=login

Response Format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/user/certificate/confirm?login=61232
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    USER_CERT_CONFIRM|LOGIN=login|\r\n

Response Format
    
    
    USER_CERT_CONFIRM|RETCODE=code description|\r\n

## Request Parameters

  * login — the login of the user whose certificate you want to confirm.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

Certificate confirmation provides extended security for accounts. It is impossible to log in using a certificate until it is confirmed. The confirmation mode is enabled in group settings.
