[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Add

[Previous](Data-Structure.md) | [Next](Add-Multiple.md)

# Adding a Symbol

Using this request you can create or change a symbol on a server.

## Rest API

Request format
    
    
    POST /api/symbol/add
    { Description of a symbol being created in JSON format }

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : { Description of the created symbol in JSON format }
    }

Example
    
    
    //--- request to the server
    POST /api/symbol/add
    {
      "Symbol" : "EURUSD",
      "Path" : "Forex\\Major\\EURUSD",
      "ISIN" : "",
      "Description" : "Euro vs US Dollar",
    ...
    }
    //--- server response
    {
      "retcode" : "0 Done",
      "answer" : {
        "Symbol" : "EURUSD",
        "Path" : "Forex\\Major\\EURUSD",
        "ISIN" : "",
        "Description" : "Euro vs US Dollar",
    ...
      }
    }

## Raw API

Request format
    
    
    SYMBOL_ADD\r\n
    Description of a symbol being created in JSON format

Response format
    
    
    SYMBOL_ADD|RETCODE=code description|\r\n
    The body of the created symbol in JSON format

## Request Parameters

This command has no parameters. Description of the symbol is passed in the JSON format as an additional command body. When adding a symbols, all its [parameters (#symbol)](Data-Structure.md#symbol) must be described.

The JSON description of the symbol passed when creating is the same as the description returned by the server.

## Response Parameters

  * retcode — if successful, the command returns [a response code](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, it will return an error code.
  * answer — parameters of the created symbol in JSON format. A complete description of the passed parameters of symbols is given in the ["Data structure" (#symbol)](Data-Structure.md#symbol) section.



## Notes

  * This command works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the command is run the presence of the symbol you are adding is checked. A key field for comparison is the name of the symbol. If such a symbol already exists, its settings are updated.
  * When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
  * Before adding, the correctness of the record is checked. If the entry is incorrect, it returns the error code [3](../../../../Return-Codes/Common-errors.md).
  * To run the command, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator ([IMTConManager::RIGHT_ADMIN (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)) and edit symbol configurations ([IMTConManager::RIGHT_CFG_SYMBOLS (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)). Otherwise, it returns the error code [8](../../../../Return-Codes/Common-errors.md).
  * To enable a newly added symbol, [restart the main trade server](../Network/Restart-Server.md).


