[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolUpdate

[Previous](SymbolUnsubscribe.md) | [Next](SymbolUpdateBatch.md)

# IMTManagerAPI::SymbolUpdate

Update symbol configuration.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolUpdate(
       IMTConSymbol*  symbol      // Symbol configuration object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolUpdate(
       CIMTConSymbol  symbol      // Symbol configuration object
       )

Python
    
    
    ManagerAPI.SymbolUpdate(
       symbol         // Symbol configuration object
       )

### Parameters

**symbol**  
[in] An object of the symbol configuration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A configuration can only be added or updated from the applications running on the main server. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned.

  * [ExecMode](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/ExecMode.md)
  * [Color](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Color.md)
  * [StopsLevel](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/StopsLevel.md)
  * [SpreadBalance](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadBalance.md)
  * [SpreadDiff](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadDiff.md)
  * [SpreadDiffBalance](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/SpreadDiffBalance.md)


