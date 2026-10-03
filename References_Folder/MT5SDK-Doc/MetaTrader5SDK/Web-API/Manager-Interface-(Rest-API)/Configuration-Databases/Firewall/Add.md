[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Firewall](../Firewall.md) / Add

[Previous](Data-Structure.md) | [Next](Delete.md)

# Add Firewall Rule

The request allows adding and updating trading platform firewall rules.

## Rest API

Request Format
    
    
    POST /api/firewall/add
    { Description of the firewall rule being created/updated in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created/updated firewall rule in JSON format }
    }

The example
    
    
    //--- request to the server
    POST /api/firewall/add
    {
      "IPFrom" : "192.168.0.1",
      "IPTo" : "192.168.0.255",
      "Action" : "2",
      "Comment" : "Local network"
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "IPFrom" : "192.168.0.1",
        "IPTo" : "192.168.0.255",
        "Action" : "2",
        "Comment" : "Local network"
      }
    }

## Raw API

Request Format
    
    
    FIREWALL_ADD|\r\n
    Description of the firewall rule being created/updated in JSON format

Response Format
    
    
    FIREWALL_ADD|RETCODE=code description|\r\n
    Description of the created/updated firewall rule in JSON format

## Request Parameters

The request has no parameters. The description of the firewall rule being created/updated is passed in JSON format as an additional body. The JSON description of the rule passed during creation is the same as the description returned by the server. The complete description of the possible parameters is provided in the ["Data structure"](Data-Structure.md) section.

## Response Parameters

  * retcode — if successful, the command returns [the response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — the description of the created firewall rule in the JSON format. The description of parameters is given in the "[Data structure](Data-Structure.md)" section



## Note

  * The request only works when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the request is run, the existence of the configuration to be added is checked. The key comparison fields are "From" and "To." If the configuration already exists, the settings of this configuration are updated.
  * When adding a configuration, the fields which are not specified in the JSON description will be filled with default values. If a default value cannot be used, the request will return the error [3](../../../../Return-Codes/Common-errors.md).
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * Before adding, the correctness of the account is checked. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the Manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have permissions to connect as an administrator and to edit firewall configurations. Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.


