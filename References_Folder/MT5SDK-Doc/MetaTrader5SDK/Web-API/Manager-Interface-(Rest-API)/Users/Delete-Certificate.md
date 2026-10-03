[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Delete Certificate

[Previous](Get-Certificate.md) | [Next](Confirm-Certificate.md)

# Delete User Certificate

The request allows deleting a user certificate.

## Rest API

Request format
    
    
    GET /api/user/certificate/delete?login=login
    POST /api/user/certificate/delete?login=login

Response format
    
    
    { "retcode" : "code description" }

Example
    
    
    //--- request to the server
    GET /api/user/certificate/delete?login=61232
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request format
    
    
    USER_CERT_DELETE|LOGIN=login|\r\n

Response format
    
    
    USER_CERT_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * login — the login of the user whose certificate you want to delete.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Note

If the extended authorization mode is used for the group to which the account belongs, then using this request the previously issued certificate can be reset.  After that, authorization with the certificate will be impossible, and a new certificate will be issued during the next attempt of the account to connect to the server.
