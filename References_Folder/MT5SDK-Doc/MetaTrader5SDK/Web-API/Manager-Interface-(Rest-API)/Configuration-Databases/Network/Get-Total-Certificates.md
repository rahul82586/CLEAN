[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Get Total Certificates

[Previous](Shift-Certificate.md) | [Next](Get-Certificate-by-Index.md)

# Get Total Certificates

The request allows receiving the number of certificates installed for access servers.

## Rest API

Request Format
    
    
    GET /api/tls_certificate/total
    POST /api/tls_certificate/total

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { "total" : "number" }
    }

The example
    
    
    //--- request to the server
    GET /api/tls_certificate/total
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { "total" : "11" }
    }

## Raw API

Request Format
    
    
    TLS_CERTIFICATE_TOTAL\r\n

Response Format
    
    
    TLS_CERTIFICATE_TOTAL|RETCODE=code description|TOTAL=number|\r\n

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * total — the number of certificates installed for access servers.



## Note

Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../Format-of-Commands.md)" section.
