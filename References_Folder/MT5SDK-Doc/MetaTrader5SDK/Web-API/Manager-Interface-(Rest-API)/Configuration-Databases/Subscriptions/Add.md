[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Subscriptions](../Subscriptions.md) / Add

[Previous](Data-Structure.md) | [Next](Delete.md)

# Add a subscription configuration.

The request allows adding and updating subscription configurations in the trading platform.

## Rest API

Request Format
    
    
    POST /api/subscription/config/add
    { Description of the subscription configuration to be created/updated, in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created/updated subscription configuration, in JSON format }
    }

Example
    
    
    //--- request to the server
    POST /api/subscription/config/add
    {
      "Name" : "Personal Manager",
      "Type" : "0",
      "Image" : "5"
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "ID" : "132591622364003374",
        "ParentID" : "0",
        "Type" : "5",
        "Name" : "Personal Manager",
        "URL" : "",
        "AgreementURL" : "",
        "Flags" : "0",
        "Control" : "0",
    ...
      }
    }

## Raw API

Request Format
    
    
    SUBSCRIPTION_CFG_ADD\r\n
    Description of the subscription configuration to be created/updated, in JSON format

Response Format
    
    
    SUBSCRIPTION_CFG_ADD|RETCODE=code description|\r\n
    "Description of the created/updated subscription configuration, in JSON format

## Request Parameters

The request has no parameters. The description of the subscription configuration being created/updated is passed in JSON format as an additional body. The JSON description of the configuration passed during creation is the same as the description returned by the server. The complete description of possible server parameters is given under the ["Data structure"](Data-Structure.md) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — description of the created server in JSON format. The description of parameters is given in the "[Data structure](../Groups/Data-Structure.md)" section



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the request is run, the existence of the server configuration to be added is checked. A key field for comparison is the configuration name. If the configuration already exists, the settings of this configuration are updated.
  * When adding a configuration, the fields which are not specified in the JSON description will be filled with default values. If a default value cannot be used, the request will return error [3](../../../../Return-Codes/Common-errors.md).
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters are not changed.
  * Record correctness is checked before it is added. If the record is incorrect, error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to access the Subscriptions section. Otherwise, error code [8](../../../../Return-Codes/Common-errors.md) is returned.


