[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SpreadDiff

[Previous](SpreadBalance.md) | [Next](SpreadDiffBalance.md)

# IMTConSymbol::SpreadDiff

Get the symbol spread difference.

C++
    
    
    INT  IMTConSymbol::SpreadDiff()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConSymbol.SpreadDiff()

Python (Manager API)
    
    
    MTConSymbol.SpreadDiff

### Return Value

Symbol spread difference. This parameter is used to set individual spread values ​​for certain groups of clients.

### Note

This method returns the base value of the spread, which is actually equal to 0. To work with spread difference of a particular group, the [IMTConGroupSymbol::SpreadDiff](../../Groups/IMTConGroupSymbol/SpreadDiff.md) method should be used.

# IMTConSymbol::SpreadDiff

Set the symbol spread difference.

C++
    
    
    MTAPIRES  IMTConSymbol::SpreadDiff(
       const INT  diff      // Spread difference
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SpreadDiff(
       int        diff      // Spread difference
       )

Python (Manager API)
    
    
    MTConSymbol.SpreadDiff

### Parameters

**diff**  
[in] Symbol spread difference.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method sets the base value of the spread difference. To set the individual spread value for certain groups of clients, the [IMTConGroupSymbol::SpreadDiff](../../Groups/IMTConGroupSymbol/SpreadDiff.md) method is used.
