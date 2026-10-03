[🏠 Document Start](../../../README.md) / [Web API](../../README.md) / [Manager Interface (Rest API)](../../Manager-Interface-(Rest-API).md) / [Clients](../Clients.md) / Get Change History

[Previous](Get.md) | [Next](Get-Identifiers.md)

# Get the History of Client Changes

The request allows receiving the history of client record changes in the specified period of time.

## Rest API

Request Format
    
    
    GET /api/client/history/get?id=identifier&from=date&to=date&author=login
    POST /api/client/history/get?id=identifier&from=date&to=date&author=login

Response Format
    
    
    {
     "retcode" : "code description",
      "answer" : [
        {
        client state description
        },
        {
        client state description
        },
        ...
      ]
    }

The example
    
    
    //--- request to the server
    GET /api/client/history/get?id=1032&from=1552395829&to=1584104703
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : [
        {
          "RecordID" : "1278",
          "PersonName" : "John",
          "PersonLastName" : "Smith"
          "ClientType" : "1",
          "ClientStatus" : "700",
          "AssignedManager" : "1000"
          ...
        },
        {
          "RecordID" : "1279",
          "PersonName" : "Mary",
          "PersonLastName" : "Anne"
          "ClientType" : "2",
          "ClientStatus" : "600",
          "AssignedManager" : "1200"
        },
        ...
      ]
    }

## Raw API

Request Format
    
    
    CLIENT_HISTORY_GET|ID=identifier|FROM=date|TO=date|AUTHOR=login|\r\n

Response Format
    
    
    CLIENT_HISTORY_GET|RETCODE=code description|\r\n
    Array of client states in JSON format

## Request Parameters

  * id — the ID of the client whose history of changes you wish to get.
  * from — the beginning of the period for which you wish to get the history of client changes. The date is specified in seconds since 01.01.1970.
  * to — the end of the period for which you wish to get the history of client changes. The date is specified in seconds since 01.01.1970.
  * author — the login of the manager account by whom the client was changed. It is used as a filter. An optional parameter. If the author is not specified or is equal to zero, changes made by any manager will be returned.



## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — an array of client states in JSON format. The complete description of passed parameters is available under the ["Data structure"](Data-Structure.md) section.



## Note

The request returns an array of client descriptions: all the client states after changes by the specified author in the specified time period.
