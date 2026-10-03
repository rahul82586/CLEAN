[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Get Backups List

[Previous](Restore-from-Archive.md) | [Next](Get-User-from-Backup.md)

# Get the List of Backups

The request allows receiving creation dates of user backups within the specified time frame.

## Rest API

Request format
    
    
    GET /api/user/backup/list?from=beginning&to=end&server=identifier
    POST /api/user/backup/list?from=beginning&to=end&server=identifier

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [ date list ]
    }

Example
    
    
    //--- request to the server
    GET /api/user/backup/list?from=1546357749&to=1574351349
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [ 1574122620,1574209020,1574250008 ]
    }

## Raw API

Request format
    
    
    USER_BACKUP_LIST|FROM=beginning|TO=end|SERVER=identifier|\r\n

Response format
    
    
    USER_BACKUP_LIST|RETCODE=code description|\r\n
    List of dates

## Request Parameters

  * from — beginning of the period for which you want to receive the list of backups. The date is specified in seconds that have elapsed since 01.01.1970.
  * to — end of the period for which you want to receive the list of backups. The date is specified in seconds that have elapsed since 01.01.1970.
  * server — identifier of the backup server from which backups are requested. Optional parameter. If not specified, copies will be requested from the first backup server in the list.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — list of dates, for which there are backups on the server. The date is specified in seconds that have elapsed since 01.01.1970.



## Notes

The received dates can be used in [/api/user/backup/get](Get-User-from-Backup.md) to request user data from specific backups.
