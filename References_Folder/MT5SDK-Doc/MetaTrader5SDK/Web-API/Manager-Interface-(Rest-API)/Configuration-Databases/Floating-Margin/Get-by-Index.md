[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Get by Index

[Previous](Get-Total.md) | [Next](Get-by-Name.md)

# Get Configuration by Index

Get one or more floating margin configurations by index in the list.

## Rest API

Request Format
    
    
    GET /api/leverage/next?index=index&count=count
    POST /api/leverage/next?index=index&count=count

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { description }
    }

Example
    
    
    //--- request to the server
    GET /api/leverage/next?index=0
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Name" : "Night rules",
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
    
    
    LEVERAGE_NEXT|INDEX=index|COUNT=count\r\n

Response Format
    
    
    LEVERAGE_NEXT|RETCODE=code description|\r\n
    Configuration body in JSON format

## Request Parameters

  * index — configuration index, starting from 0.
  * count — the number of configurations to which you wish to receive. If the parameter is not set or is equal to 1, the query returns one object with a configuration description. If count > 1, the query will return an array of objects. For example, when sending a query with parameters ?index=1&count=3, you will get three configurations, from the second to the fourth one.



## Response Parameters

  * retcode — if successful, the command returns [response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned. If an index of a non-existent symbol is requested, the response code [13](../../../../Return-Codes/Common-errors.md) is returned.
  * answer — configuration in JSON format. The full description of the passed symbol parameters is provided in the [Data structure](Data-Structure.md) section.


