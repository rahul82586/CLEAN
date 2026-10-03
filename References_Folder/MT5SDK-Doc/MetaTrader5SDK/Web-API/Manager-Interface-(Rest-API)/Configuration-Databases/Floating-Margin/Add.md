[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Floating Margin](../Floating-Margin.md) / Add

[Previous](Data-Structure.md) | [Next](Delete.md)

# Add Configuration

Create or update the floating margin configuration on the server.

## Rest API

Request Format
    
    
    POST /api/leverage/add
    { Description of the configuration to be created, in JSON format }

Response Format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created configuration, in JSON format }
    }

Example
    
    
    //--- request to the server
    POST /api/leverage/add
    {
      "Name" : "Night rules",
      "Rules" : [
        {
          "Name": "Forex symbols",
          "Description": "Night rules for Forex symbols",
          "RangeMode": "0",
    ...
    }
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
    
    
    LEVERAGE_ADD\r\n
    Description of the configuration to be created, in JSON format

Response Format
    
    
    LEVERAGE_ADD|RETCODE=code description|\r\n
    The body of the created configuration, in JSON format

## Request Parameters

This command has no parameters. The description of the configuration to be created is transmitted in JSON format as an additional command body. When adding a configuration, you must describe all of it [parameters](Data-Structure.md).

The JSON description of the configuration passed during creation is similar to the description returned by the server. For example:

## Response Parameters

  * retcode — if successful, the command returns [response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, the code of the encountered error is returned.
  * answer — parameters of the created configuration in JSON format. The full description of the passed symbol parameters is provided in the [Data structure](Data-Structure.md) section.



## Note

  * This command works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * During command execution, the existence of the configuration to be added is checked. The key field for comparison is the name. If the configuration already exists, the settings of this configuration are updated.
  * When a configuration is updated, only those parameters that are explicitly specified in the JSON description are replaced. Other parameters stay unchanged.
  * A record is validated before being added. If the record is incorrect, error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the command, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator and to edit leverage configurations. Otherwise, error code [8](../../../../Return-Codes/Common-errors.md) is returned.


