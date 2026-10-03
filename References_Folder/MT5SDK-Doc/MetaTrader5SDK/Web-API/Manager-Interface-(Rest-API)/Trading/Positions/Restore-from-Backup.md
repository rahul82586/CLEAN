[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Restore from Backup

[Previous](Get-from-Backup.md) | [Next](Check.md)

# Restore Positions from Backup

The request allows restoring positions from backup databases.

## Rest API

Request Format
    
    
    POST /api/position/backup/restore
    { Position description in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/position/backup/restore
    {
       "Position" : "618",
       "ExternalID" : "",
       "Login" : "104366",
       ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Position" : "618",
        "ExternalID" : "",
        "Login" : "104366",
        ...
      }
    }

## Raw API

Request Format
    
    
    POSITION_BACKUP_RESTORE|\r\n
    Description of a position to be restored, in JSON format

Response Format
    
    
    POSITION_BACKUP_RESTORE|RETCODE=code description|\r\n
    Description of a restored position in JSON format

## Request Parameters

The request has no parameters. The description of the position to be restored is passed in JSON format as an additional body. To receive a position description from the backup, use the [/api/position/backup/get](Get-from-Backup.md) request.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — restored position parameters in JSON format. The complete description of position parameters is provided under the [Data Structure](Data-Structure.md) section.



## Note

Restored positions are not deleted from the backup.
