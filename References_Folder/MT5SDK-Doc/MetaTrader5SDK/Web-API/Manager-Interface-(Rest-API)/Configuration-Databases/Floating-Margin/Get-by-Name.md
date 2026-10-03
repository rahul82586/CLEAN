[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Get by Name

[Previous](Get-by-Index.md) | [Next](../Firewall.md)

# Gets configuration by name

Get one or more floating margin configurations by name.

## Rest API

Request Format
    
    
    GET /api/leverage/get?name=name
    POST /api/leverage/get?name=name

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/leverage/get?name=Leverage
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Leverage",
        "Rules" : [
          {
            "Name": "Forex symbols",
            "Description": "Night rules for Forex symbols",
            "RangeMode": "0",
    ...
      }
    }

## Raw API

Request Format
    
    
    LEVERAGE_GET|NAME=name\r\n

Response Format
    
    
    LEVERAGE_GET|RETCODE=code description|\r\n
    Configuration body in JSON format

## Request Parameters

  * name — name of the configuration to be received.



## Response Parameters

  * retcode — if successful, the command returns [response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a non-existent symbol is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — configuration in JSON format. The full description of the passed symbol parameters is provided in the [Data structure](Data-Structure.md) section.


