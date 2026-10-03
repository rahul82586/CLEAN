[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Positions](../Positions.md) / Get Backups List

[Previous](Delete.md) | [Next](Get-from-Backup.md)

# Get the List of Backups

The request allows receiving creation dates of position backups within the specified time frame.

## Rest API

Request Format
    
    
    GET /api/position/backup/list?from=beginning&to=end&server=identifier
    POST /api/position/backup/list?from=beginning&to=end&server=identifier

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ date list ]
    }

Example
    
    
    //--- request to the server
    GET /api/position/backup/list?from=1546357749&to=1574351349
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 1574122620,1574209020,1574250008 ]
    }

## Raw API

Request Format
    
    
    POSITION_BACKUP_LIST|FROM=beginning|TO=end|SERVER=identifier|\r\n

Response Format
    
    
    POSITION_BACKUP_LIST|RETCODE=code description|\r\n
    List of dates

## Request Parameters

  * from — beginning of the period for which you want to receive the list of backups. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — end of the period for which you want to receive the list of backups. The date is specified in seconds that have elapsed since 01.01.1970.
  * server — identifier of the backup server from which backups are requested. Optional parameter. If not specified, copies will be requested from the first backup server in the list.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — list of dates, for which there are backups on the server. The date is specified in seconds that have elapsed since 01.01.1970.



## Note

The received dates can be used in [/api/position/backup/get](Get-from-Backup.md) to request position data from specific backups.
