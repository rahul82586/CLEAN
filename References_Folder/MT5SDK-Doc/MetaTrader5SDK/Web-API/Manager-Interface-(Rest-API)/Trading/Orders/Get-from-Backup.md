[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Get from Backup

[Previous](Get-Backups-List.md) | [Next](Restore-from-Backup.md)

# Get Orders from Backup

The request allows receiving information about one or more orders from a specific backup on the server.

## Rest API

Request Format
    
    
    GET /api/order/backup/get?backup=date&login=login&ticket=ticket&from=beginning&to=end&server=identifier
    POST /api/order/backup/get?backup=date&login=login&ticket=ticket&from=beginning&to=end&server=identifier

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ description of orders ]
    }

Example
    
    
    //--- request to the server
    GET /api/order/backup/get?backup=1574122620&login=104366
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        { 
         "Order" : "12832917",
         "ExternalID" : "",
         "Login" : "104366",
         ...
        },
        { 
         "Order" : "12832918",
         "ExternalID" : "",
         "Login" : "104366",
         ...
        },
    ...
      ]
    }

## Raw API

Request Format
    
    
    ORDER_BACKUP_GET|BACKUP=date|LOGIN=login|TICKET=ticket|FROM=date|TO=date|SERVER=identifier|\r\n

Response Format
    
    
    ORDER_BACKUP_GET|RETCODE=code description|\r\n
    Description of orders in JSON format

## Request Parameters

  * backup — backup copy date. To get the list of available backups, use the [/api/order/backup/list](Get-Backups-List.md) request.
  * server — identifier of the backup server from which the order is requested. Optional parameter. If not specified, data will be requested from the first backup server in the list.
  * login — the login of the user whose orders should be retrieved from the backup database. The parameter is required if the order ticket is not specified in the request.
  * ticket — the ticket of the order which you want to obtain from the backup database.
  * from — the beginning of the period for requesting orders. The date is specified in seconds that have since 01.01.1970. Th-s parameter cannot be used together with the 'ticket' parameter.
  * from — the end of the period for requesting orders. The date is specified in seconds that have since 01.01.1970. Th-s parameter cannot be used together with the 'ticket' parameter.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — order parameters in JSON format. The full description of passed order parameters is available under the ["Data structure"](Data-Structure.md) section.


