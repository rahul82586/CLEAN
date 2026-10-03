[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / SymbolAdd

[Previous](CommissionGet.md) | [Next](SymbolUpdate.md)

# IMTConGroup::SymbolAdd

Add a symbol setting for a group.

C++
    
    
    MTAPIRES  IMTConGroup::SymbolAdd(
       IMTConGroupSymbol*  symbol      // An object of the symbol setting
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.SymbolAdd(
       CIMTConGroupSymbol  symbol      // An object of the symbol setting
       )

Python (Manager API)
    
    
    MTConGroup.SymbolAdd(
       symbol              # An object of the symbol setting
       )

### Parameters

**symbol**  
[in] An object of the symbol setting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
