[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Delete Certificate

[Previous](Add-Certificate.md) | [Next](Shift-Certificate.md)

# Delete Certificate

The request allows deleting SSL certificates from access servers.

## Rest API

Request Format
    
    
    GET /tls_server_delete?index=indices
    POST /tls_server_delete?index=indices

Response Format
    
    
    { "retcode" : "code description" }

The example
    
    
    //--- request to the server
    POST /api/tls_certificate/delete?index=0
    //--- server response
    { "retcode" : "0 Done" }

## Raw API

Request Format
    
    
    TLS_CERTIFICATE_DELETE|INDEX=indices|\r\n

Response Format
    
    
    TLS_CERTIFICATE_DELETE|RETCODE=code description|\r\n

## Request Parameters

  * index — position of certificate to be deleted, starting from 0. Multiple indices can be specified as separated by commas.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.



## Disclaimer

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit network configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.
  * Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../Format-of-Commands.md)" section.


