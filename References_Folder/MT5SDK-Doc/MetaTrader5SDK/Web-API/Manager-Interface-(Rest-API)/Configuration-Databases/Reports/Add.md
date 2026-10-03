[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Reports](../Reports.md) / Add

[Previous](Data-Structure.md) | [Next](Delete.md)

# Add Report

The request allows adding and updating report configurations in the trading platform.

## Rest API

Request Format
    
    
    POST /api/report/add
    { Description of the configuration to be created/updated, in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created/updated configuration in JSON format }
    }

The example
    
    
    //--- request to the server
    POST /api/report/add
    {
      "Name" : "Daily Trades",
      "Server" : "1",
      "Template" : "Daily Trades",
      "Enable" : "1",
      "Params" : [
        {
          "Type" : "0",
          "Name" : "Currency",
          "Value" : "USD"
        }
      ]
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Daily Trades",
        "Server" : "1",
        "Template" : "Daily Trades",
        "Enable" : "1",
        "Params" : [
          {
            "Type" : "0",
            "Name" : "Currency",
            "Value" : "USD"
          }
        ]
      }
    }

## Raw API

Request Format
    
    
    REPORT_ADD|\r\n
    Description of the configuration to be created/updated, in JSON format

Response Format
    
    
    REPORT_ADD|RETCODE=code description|\r\n
    Description of the created/updated configuration in JSON format

## Request Parameters

The request has no parameters. The description of the report configuration being created/updated is passed in JSON format as an additional body. The JSON description of the configuration passed during creation is the same as the description returned by the server. The complete description of the possible parameters is provided in the ["Data structure"](../Data-Feeds/Data-Structure.md) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the created report configuration in JSON format. The description of parameters is given in the "[Data structure](../Data-Feeds/Data-Structure.md)" section



## Disclaimer

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * During request execution, the existence of the configuration to be added is checked. The key field to check is "Name". If the configuration already exists, the settings of this configuration are updated.
  * When adding a configuration, the fields which are not specified in the JSON description will be filled with default values. If a default value cannot be used, the request will return the error [3](../../../../Return-Codes/Common-errors.md).
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * Before adding, the correctness of the account is checked. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit report configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


