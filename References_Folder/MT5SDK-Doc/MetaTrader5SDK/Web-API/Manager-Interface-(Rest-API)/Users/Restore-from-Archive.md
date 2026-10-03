[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Users](../Users.md) / Restore from Archive

[Previous](Get-Multiple-from-Archive.md) | [Next](Get-Backups-List.md)

# Restore User from Archive

The request allows restoring users from archive or backup.

## Rest API

Request format
    
    
    POST /api/user/restore
    { User description in JSON format }

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    POST /api/user/restore
    {
      "Login" : "954402",
      "Group" : "demoforex",
      "CertSerialNumber" : "0",
      "Rights" : "2531",
      "MQID" : "5CD369A9",
      "Registration" : "1572956466",
      "LastAccess" : "1572956466",
      "LastPassChange" : "1572956466",
      "Name" : "JohnSmith",
      "Company" : "Individual",
    ...
    }
     
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : { 
        "Login" : "954402",
        "Group" : "demoforex",
        "CertSerialNumber" : "0",
        "Rights" : "2531",
        "MQID" : "5CD369A9",
        "Registration" : "1572956466",
        "LastAccess" : "1572956466",
        "LastPassChange" : "1572956466",
        "Name" : "JohnSmith",
        "Company" : "Individual",
    ...
      }
    }

## Raw API

Request format
    
    
    USER_RESORE|\r\n
    Description of a user to be restored in JSON format

Response format
    
    
    USER_RESORE|RETCODE=code description|\r\n
    Restored user description in JSON format

## Request Parameters

The request has no parameters. The description of the user to be restored is passed in JSON format as an additional body. To get a user description from archive or backup, use the [/api/user/backup/get](Get-User-from-Backup.md) request.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — parameters of a restored user in JSON format. The full description of passed client parameters is available under the ["Data structure"](Data-Structure.md) section.



## Note

  * Restored users are not deleted from the archive.
  * When a recovered account is once again moved to archive or backup, new data replace previously stored data.


