[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / Add

[Previous](Data-Structure.md) | [Next](Delete.md)

# Add Spread

The request allows adding and updating spread configurations in the trading platform.

## Rest API

Request Format
    
    
    POST /api/spread/add
    { Description of the configuration to be created/updated, in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created/updated configuration in JSON format }
    }

The example
    
    
    //--- request to the server
    POST /api/spread/add
    {
     "ID" : "2",
     "MarginType" : "1",
     "LegsA" : [
       {
        "Mode" : "1",
        "Symbol" : "APL-9.20",
        "TimeFrom" : "1564490700",
        "TimeTo" : "1590842700",
        "Ratio" : "1.00000000"
       }
     ],
     "LegsB" : [
       {
        "Mode" : "1",
        "Symbol" : "APL-12.20",
        "TimeFrom" : "1564490700",
        "TimeTo" : "1590842700",
        "Ratio" : "1.00000000"
       }
     ]
    }
     }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
      "ID" : "2",
      "Flags" : "0",
      "MarginInitial" : "0.00000000",
      "MarginMaintenance" : "0.00000000",
      "MarginType" : "1",
      "LegsA" : [
        {
         "Mode" : "1",
         "Flags" : "0",
         "Symbol" : "APL-9.20",
         "TimeFrom" : "1564490700",
         "TimeTo" : "1590842700",
         "Ratio" : "1.00000000"
       }
      ],
      "LegsB" : [
        {
         "Mode" : "1",
         "Flags" : "0",
         "Symbol" : "APL-12.20",
         "TimeFrom" : "1564490700",
         "TimeTo" : "1590842700",
         "Ratio" : "1.00000000"
        }
      ]
     }
    }

## Raw API

Request Format
    
    
    SPREAD_ADD|\r\n
    Description of the configuration to be created/updated, in JSON format

Response Format
    
    
    SPREAD_ADD|RETCODE=code description|\r\n
    Description of the created/updated configuration in JSON format

## Request Parameters

The request has no parameters. The description of the spread configuration being created/updated is passed in JSON format as an additional body. The JSON description of the spread configuration passed during creation is the same as the description returned by the server. The complete description of the possible parameters is provided in the ["Data structure"](Data-Structure.md) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the created spread configuration in JSON format. The description of parameters is given in the "[Data structure](Data-Structure.md)" section



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the request is run, the existence of the configuration to be added is checked. The key field to check is "Login". If the configuration already exists, the settings of this configuration are updated.
  * When adding a configuration, the fields which are not specified in the JSON description will be filled with default values. If a default value cannot be used, the request will return the error [3](../../../../Return-Codes/Common-errors.md).
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * Before adding, the correctness of the account is checked. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit spread configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


