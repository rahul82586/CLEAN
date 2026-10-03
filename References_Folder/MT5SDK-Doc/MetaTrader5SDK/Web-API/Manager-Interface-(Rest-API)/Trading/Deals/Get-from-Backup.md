[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Trading](../../Trading.md) / [Deals](../Deals.md) / Get from Backup

[Previous](Get-Backups-List.md) | [Next](Restore-from-Backup.md)

# Get Deals from Backup

The request allows receiving information about one or more deals from a specific backup on the server.

## Rest API

Request Format
    
    
    GET /api/deal/backup/get?backup=date&login=login&from=beginning&to=end&server=identifier
    POST /api/deal/backup/get?backup=date&login=login&from=beginning&to=end&server=identifier

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : [ description of deals ]
    }

Example
    
    
    //--- request to the server
    GET /api/deal/backup/get?backup=1574122620&login=104366
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        { 
         "Deal" : "11918642",
         "ExternalID" : '',
         "Login" : "104366",
         ...
        },
        { 
         "Deal" : "11918643",
         "ExternalID" : "",
         "Login" : "104366",
         ...
        },
    ...
      ]
    }

## Raw API

Request Format
    
    
    DEAL_BACKUP_GET|BACKUP=date|LOGIN=login|FROM=date|TO=date|SERVER=identifier|\r\n

Response Format
    
    
    DEAL_BACKUP_GET|RETCODE=code description|\r\n
    Description of deals in JSON format

## Request Parameters

  * backup — backup copy date. To get the list of available backups, use the [/api/deal/backup/list](Get-Backups-List.md) request.
  * server — identifier of the backup server from which the deal is requested. Optional parameter. If not specified, data will be requested from the first backup server in the list.
  * login — the login of the user whose deals should be retrieved from the backup database. Mandatory parameter.
  * from — the beginning of the period for requesting deals. The date is specified in seconds that have since 01.01.1970. Optional parameter.
  * from — the end of the period for requesting deals. The date is specified in seconds that have since 01.01.1970. Optional parameter.



## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — deal parameters in JSON format. The complete description of the passed deal parameters is given under the [Data structure](Data-Structure.md) section.


