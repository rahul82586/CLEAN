[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SpreadDiff

[Previous](ExpirFlagsDefault.md) | [Next](SpreadDiffDefault.md)

# IMTConGroupSymbol::SpreadDiff

Get a difference between a symbol spread for the group and [the default spread](../../Symbols/IMTConSymbol/Spread.md).

C++
    
    
    INT  IMTConGroupSymbol::SpreadDiff()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGroupSymbol.SpreadDiff()

Python (Manager API)
    
    
    MTConGroupSymbol.SpreadDiff

### Return Value

Symbol spread difference.

### Note

Price conversion settings for the group ([IMTConGroupSymbol::SpreadDiff](SpreadDiff.md) and [IMTConGroupSymbol::SpreadDiffBalance](SpreadDiffBalance.md)) are applied after basic symbol settings ([IMTConSymbol::Spread](../../Symbols/IMTConSymbol/Spread.md) and [IMTConSymbol::SpreadBalance](../../Symbols/IMTConSymbol/SpreadBalance.md)).

# IMTConGroupSymbol::SpreadDiff

Set a difference between a symbol spread for the group and [the default spread](../../Symbols/IMTConSymbol/Spread.md).

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SpreadDiff(
       const INT  spread      // Spread difference
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SpreadDiff(
       int        spread      // Spread difference
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SpreadDiff

### Parameters

**spread**  
[in] Symbol spread difference.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Price conversion settings for the group ([IMTConGroupSymbol::SpreadDiff](SpreadDiff.md) and [IMTConGroupSymbol::SpreadDiffBalance](SpreadDiffBalance.md)) are applied after basic symbol settings ([IMTConSymbol::Spread](../../Symbols/IMTConSymbol/Spread.md) and [IMTConSymbol::SpreadBalance](../../Symbols/IMTConSymbol/SpreadBalance.md)).
