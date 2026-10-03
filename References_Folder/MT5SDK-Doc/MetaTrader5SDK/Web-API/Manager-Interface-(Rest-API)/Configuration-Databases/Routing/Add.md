[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Routing](../Routing.md) / Add

[Previous](Data-Structure.md) | [Next](Delete.md)

# Add Routing Rule

The request allows adding and updating routing rules in the trading platform.

## Rest API

Request Format
    
    
    POST /api/route/add
    { Description of the configuration to be created/updated, in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created/updated configuration in JSON format }
    }

The example
    
    
    //--- request to the server
    POST /api/route/add
    {
      "Name" : "Send to gateway",
      "Mode" : "1",
      "Request" : "33554431",
      "Type" : "255",
      "Action" : "1001",
      "Conditions" : [
        {
         "Condition" : "1000",
         "Rule" : "3",
         "ValueUInt" : "1815998",
        }
      ],
      "Dealers" : [
        {
         "Login" : "227"
        }
      ]
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Send to gateway",
        "Mode" : "1",
        "Request" : "33554431",
        "Type" : "255",
        "Flags" : "0",
        "Action" : "1001",
        "ActionValueInt" : "0",
        "ActionValueUInt" : "0",
        "ActionValueFloat" : "0.00",
        "ActionValueString" : "",
        "Conditions" : [
          {
           "Condition" : "1000",
           "Rule" : "3",
           "ValueInt" : "0",
           "ValueUInt" : "1815998",
           "ValueFloat" : "0.00",
           "ValueString" : ""
         }
      ]
      "Dealers" : [
        {
         "Login" : "227",
         "Name" : "MetaTrader 5 Gateway"
        }
      ]
      }
    }

## Raw API

Request Format
    
    
    ROUTE_ADD|\r\n
    Description of the configuration to be created/updated, in JSON format

Response Format
    
    
    ROUTE_ADD|RETCODE=code description|\r\n
    Description of the created/updated configuration in JSON format

## Request Parameters

The request has no parameters. The description of the rule being created/updated is passed in JSON format as an additional body. The JSON description of the rule passed during creation is the same as the description returned by the server. The complete description of the possible parameters is provided in the ["Data structure"](Data-Structure.md) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — the description of the created routing rule in JSON format. The description of parameters is given in the "[Data structure](../Managers/Data-Structure.md)" section



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the request is run, the existence of the configuration to be added is checked. The key field to check is "Name". If the configuration already exists, the settings of this configuration are updated.
  * When adding a configuration, the fields which are not specified in the JSON description will be filled with default values. If a default value cannot be used, the request will return the error [3](../../../../Return-Codes/Common-errors.md).
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * Before adding, the correctness of the account is checked. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit routing configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


