[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Symbols](../Symbols.md) / SymbolRequestArray

[Previous](SymbolRequest.md) | [Next](SymbolExist.md)

# IMTManagerAPI::SymbolRequestArray

Request from the server an array of symbols by mask.

C++
    
    
    MTAPIRES  IMTManagerAPI::SymbolRequestArray(
       LPCWSTR             mask,    // Mask
       LPCWSTR             group,   // Group name
       IMTConSymbolArray*  symbols  // Symbols array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.SymbolRequestArray(
       string              mask,    // Mask
       string              group,   // Group name
       CIMTConSymbolArray  symbols  // Symbols array object
       )

Python
    
    
    ManagerAPI.SymbolRequestArray(
       mask,               # Mask
       group               # Group name
       )

### Parameters

**mask**  
[in] One or more symbols separated by commas. Specify the full name of the symbol, including the path. For example, Forex\EURUSD. The symbol name can be obtained by using theIMTConSymbol::Symbolmethod. Symbols can also be specified using wildcard characters: "*" (any value) and "!" (exclude). For example, Forex\*,!Forex\EURUSD — all symbols in the Forex subgroup except EURUSD. The maximum length of the mask is 512 characters (including the end-of-line character).

**group**  
[in] The name of the group whose symbol settings should be used (IMTConGroupSymbol). The method will pass symbol configurations based on how they are redefined for the specified group. If the parameter is null, the method will pass the basic symbol settings.

**symbols**  
[out] Symbols array objectIMTConSymbolArray. Must be previously created by using theIMTManagerAPI::SymbolCreateArrayobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
