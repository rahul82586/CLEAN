[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / MarginInitial

[Previous](MarginType.md) | [Next](MarginMaintenance.md)

# IMTConSpread::MarginInitial

Getting the value of the parameter for setting an initial margin.

C++
    
    
    LPCWSTR  IMTConSpread::MarginInitial()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSpread.MarginInitial()

Python (Manager API)
    
    
    MTConSpread.MarginInitial

### Return Value

The value of the parameter for setting an initial margin.

# IMTConSpread::MarginInitial

Setting the value of the parameter for setting an initial margin.

C++
    
    
    MTAPIRES  IMTConSpread::MarginInitial(
       LPCWSTR  path      // The value for setting an initial margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.MarginInitial(
       string   path      // The value for setting an initial margin
       )

Python (Manager API)
    
    
    MTConSpread.MarginInitial

### Parameters

**path**  
[in] The value of the parameter for setting an initial margin.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

According to the margin charging type ([IMTConSpread:MarginType](MarginType.md)), different values are specified in this method:

  * MARGIN_TYPE_VALUE — the values of the initial margin that will be charged at the specified combination of positions;
  * MARGIN_TYPE_MAXIMAL — the value is not specified ([IMTConSpread::MarginInitial](MarginInitial.md) method is not used);
  * MARGIN_TYPE_CME_INTER — initial margin ratio (multiplier). The total margin value will be defined by summing up the margin requirements for all symbols of the spread (by [IMTConSymbol::MarginInitial](../../Symbols/IMTConSymbol/MarginInitial.md) value or the appropriate value redefined for [client group](../../Groups/IMTConGroupSymbol.md)) and multiplying the total value by the specified ratio;
  * MARGIN_TYPE_CME_INTRA — the difference between the total margin of A leg symbols and the total margin of B leg symbols is calculated (the difference in absolute magnitude is used, so that it does matter what leg is a deductible one). The value specified in [IMTConSpread::MarginInitial](MarginInitial.md) parameter is added to the obtained difference.


