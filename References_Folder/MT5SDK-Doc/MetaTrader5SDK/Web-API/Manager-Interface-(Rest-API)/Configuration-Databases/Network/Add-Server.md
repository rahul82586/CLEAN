[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Network](../Network.md) / Add Server

[Previous](Data-Structure.md) | [Next](Delete-Server.md)

# Add Server

The request allows adding and updating server configurations in the platform.

## Rest API

Request format
    
    
    POST /api/server/add
    { Description of the server being created/updated in JSON format }

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created/updated server in JSON format }
    }

Example
    
    
    //--- request to the server
    POST /api/server/add
    {
      "Type" : "1",
      "Name" : "Trade Server",
      "Login" : "50"
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Type": "1",
        "Name": "Test Web",
        "Address": "",
        "Login": "50",
        "Adapter": "",
        "ServiceTime": "227",
        "Adapters": [],
        "Addresses": [],
    ...
      }
    }

## Raw API

Request format
    
    
    SERVER_ADD|\r\n
    Description of the server being created/updated in JSON format

Response format
    
    
    SERVER_ADD|RETCODE=code description|\r\n
    Created/updated server body in JSON format

## Request Parameters

The request has no parameters. The description of the server being created/updated is passed in JSON format as an additional body. The JSON description of the server passed during creation is the same as the description returned by the server. The complete description of possible server parameters is given under the ["Data structure"](Data-Structure.md) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the created server in JSON format. The description of passed parameters is provided under the "[Data structure](../Groups/Data-Structure.md)" section



## Notes

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the request is run, the existence of the server configuration to be added is checked. The key field for comparison is the server ID. If the configuration already exists, the settings of this configuration are updated.
  * When adding a configuration, the fields which are not specified in the JSON description will be filled with default values. If a default value cannot be used, the request will return the error [3](../../../../Return-Codes/Common-errors.md).
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * The record correctness is checked before the configuration is added. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit network configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


