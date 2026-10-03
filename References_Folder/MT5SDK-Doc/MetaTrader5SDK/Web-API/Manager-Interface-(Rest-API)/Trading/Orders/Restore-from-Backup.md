[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Orders](../Orders.md) / Restore from Backup

[Previous](Get-from-Backup.md) | [Next](Reopen-Order.md)

# Restore Order from Archive

The request allows restoring orders from backup databases.

## Rest API

Request Format
    
    
    POST /api/order/backup/restore
    { Order description in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/order/backup/restore
    {
      "Order" : "12832917",
      "ExternalID" : "",
      "Login" : "104366",
       ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Order" : "12832917",
        "ExternalID" : "",
        "Login" : "104366",
        ...
      }
    }

## Raw API

Request Format
    
    
    ORDER_BACKUP_RESTORE|\r\n
    Description of an order to be restored, in JSON format

Response Format
    
    
    ORDER_BACKUP_RESTORE|RETCODE=code description|\r\n
    Description of the restored order in JSON format

## Request Parameters

The request has no parameters. The description of the order to be restored is passed in JSON format as an additional body. To receive an order description from the backup, use the [/api/order/backup/get](Get-from-Backup.md) request.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — recovered order parameters in JSON format. The full description of order parameters is available under the [Data Structure](Data-Structure.md) section.



## Note

Restored orders are not deleted from the backup.
