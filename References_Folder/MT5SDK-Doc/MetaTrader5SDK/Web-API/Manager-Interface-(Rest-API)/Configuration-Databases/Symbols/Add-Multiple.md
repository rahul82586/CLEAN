[🏠 Document Start](../../../../README.md) / [Web API](../../../README.md) / [Manager Interface (Rest API)](../../../Manager-Interface-(Rest-API).md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / Add Multiple

[Previous](Add.md) | [Next](Delete.md)

# Add Multiple Symbols

The request allows creating or updating multiple symbols on a server.

## Rest API

Request format
    
    
    POST /api/symbol/add_batch
    [ Descriptions of symbols to be created, in JSON format ]

Response format
    
    
    {
     "retcode" : "code description",
     "answer" : [ Description of created symbols in JSON format ]
    }

Example
    
    
    //--- request to the server
    POST /api/symbol/add
    [
      {
       "Symbol" : "EURUSD",
       "Path" : "Forex\\Major\\EURUSD",
       "ISIN" : "",
       "Description" : "Euro vs US Dollar",
       ...
      },
      {
       "Symbol" : "GBPUSD",
       "Path" : "Forex\\Major\\GBPUSD",
       "ISIN" : "",
       "Description" : "Pound vs US Dollar",
       ...
      },
    ]
    //--- server response
    [
      {
       "retcode" : "0 Done",
       "answer" : {
         "Symbol" : "EURUSD",
         "Path" : "Forex\\Major\\EURUSD",
         "ISIN" : "",
         "Description" : "Euro vs US Dollar",
         ...
         }
      },
      {
       "retcode" : "0 Done",
       "answer" : {
         "Symbol" : "GBPUSD",
         "Path" : "Forex\\Major\\GBPUSD",
         "ISIN" : "",
         "Description" : "Pound vs US Dollar",
         ...
         }
      },
    ]

## Raw API

Request format
    
    
    SYMBOL_ADD_BATCH\r\n
    Descriptions of symbols to be created, in JSON format

Response format
    
    
    SYMBOL_ADD_BATCH|RETCODE=code description|\r\n
    Description of created symbols in JSON format

## Request Parameters

The request has no parameters. The description of the symbols is passed in the JSON format as an additional body. When adding a symbol, all its [parameters (#symbol)](Data-Structure.md#symbol) must be described.

The JSON description of the symbols passed when creating is the same as the description returned by the server.

## Response Parameters

  * retcode — if successful, the command returns [the response code ](../../../../Return-Codes/Successful-completion.md) 0\. Otherwise, an error code is returned.
  * answer — parameters of created symbols, in JSON format. The full description of passed symbol parameters is available under the ["Data structure" (#symbol)](Data-Structure.md#symbol) section.



## Note

  * This request works only when connected to the main trade server. Otherwise error [12001](../../../../Return-Codes/API.md) is returned.
  * When the request is run, the existence of the symbols to be added is checked. A key field for comparison is the symbol name. If such a symbol already exists, its settings are updated.
  * When you update the configuration, only those symbol parameters that are explicitly specified in the JSON description, are changed. Other parameters stay unchanged.
  * The record correctness is checked before the configuration is added. If the record is incorrect, the error code [3](../../../../Return-Codes/Common-errors.md) is returned.
  * To run the request, [the manager account](../../Text-Protocol-(Raw-API)/Authentication.md#client-start) must have rights to connect as an administrator ([IMTConManager::RIGHT_ADMIN (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)) and edit symbol configurations ([IMTConManager::RIGHT_CFG_SYMBOLS (#enmanagerrights)](../../../../Configuration-Interfaces/Managers/IMTConManager/Enumerations.md#enmanagerrights)). Otherwise, the error code [8](../../../../Return-Codes/Common-errors.md) is returned.
  * To activate the newly added symbols, [restart the main trade server](../Network/Restart-Server.md).


