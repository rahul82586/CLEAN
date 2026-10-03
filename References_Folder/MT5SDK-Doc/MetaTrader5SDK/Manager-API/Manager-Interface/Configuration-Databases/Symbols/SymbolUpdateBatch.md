[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUpdateBatch

[Previous](SymbolUpdate.md) | [Next](SymbolTotal.md)

# IMTManagerAPI::SymbolUpdateBatch

Update multiple symbol configurations.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolUpdateBatch(
       IMTConSymbol**    configs,      // Array of configurations
       const UINT        config_total, // Number of configurations in the array
       MTAPIRES*         results       // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolUpdateBatch(
       CIMTConSymbol[]   configs,      // Array of configurations
       MTRetCode[]       results       // Array of results
       )

Python
    
    
    ManagerAPI.SymbolUpdateBatch(
       configs           # Array of configurations
       )

### Parameters

**configs**  
[in] A pointer to an array of configurations which you want to add/update.

**config_total**  
[in] The number of configurations in the 'configs' array.

**results**  
[out] An array with the results of each configuration applying on the server.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned. The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code is an indication of successful change sending to a server; change applying results are passed in the 'results' parameter.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.

  * [ExecMode](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md)
  * [Color](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Color.md)
  * [StopsLevel](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/StopsLevel.md)
  * [SpreadBalance](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadBalance.md)
  * [SpreadDiff](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadDiff.md)
  * [SpreadDiffBalance](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadDiffBalance.md)


