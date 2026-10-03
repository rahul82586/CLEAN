[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Restore from Backup

[Previous](Get-from-Backup.md) | [Next](../Positions.md)

# Restore Deals from Backup

The request allows restoring deals from backup databases.

## Rest API

Request Format
    
    
    POST /api/deal/backup/restore
    { Deal description in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/deal/backup/restore
    {
       "Deal" : "11918642",
       "ExternalID" : '',
       "Login" : "104366",
       ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Deal" : "11918642",
        "ExternalID" : '',
        "Login" : "104366",
        ...
      }
    }

## Raw API

Request Format
    
    
    DEAL_BACKUP_RESTORE|\r\n
    Description of a deal to be restored, in JSON format

Response Format
    
    
    DEAL_BACKUP_RESTORE|RETCODE=code description|\r\n
    Description of a restored deal in JSON format

## Request Parameters

The request has no parameters. The description of the deal to be restored is passed in JSON format as an additional body. To receive a deal description from the backup, use the [/api/deal/backup/get](Get-from-Backup.md) request.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — restored deal parameters in JSON format. The complete description of deal parameters is given under the [Data structure](Data-Structure.md) section.



## Note

Restored deals are not deleted from the backup.
