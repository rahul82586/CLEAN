[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Get Certificate by Index

[Previous](Get-Total-Certificates.md) | [Next](../Time.md)

# Get Certificate Description by Index

The request allows obtaining details of a certificate installed for access servers, by index.

## Rest API

Request Format
    
    
    GET /api/tls_certificate/next?index=index
    POST /api/tls_certificate/next?index=index

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

The example
    
    
    //--- request to the server
    GET /api/tls_certificate/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        Timestamp: '131946323420236133',
        Name: '*.broker.com',
        Thumbprint: '151de69e0c138a1h9a96f3596a61db3d789e85f6'
      }
    }

## Raw API

Request Format
    
    
    TLS_CERTIFICATE_NEXT|INDEX=index\r\n

Response Format
    
    
    TLS_CERTIFICATE_NEXT|RETCODE=code description|\r\n
    Certificate description in JSON format

## Request Parameters

  * index — certificate index starting with 0.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a nonexistent group is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — certificate description in JSON format. The complete description of passed parameters is available under the ["Data structure" (#certificate)](Data-Structure.md#certificate) section.



## Note

Certificates are required for connection to access servers using the HTTPS protocol. This enables sending of [Web API](../../../README.md) commands to a server as ordinary GET and POST requests. For details please visit the "[Requests via HTTPS](../../../Format-of-Commands.md)" section.
