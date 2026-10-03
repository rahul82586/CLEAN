[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / MarginMaintenance

[Previous](MarginInitial.md) | [Next](ALegAdd.md)

# IMTConSpread::MarginMaintenance

Getting the value of the parameter for setting a maintenance margin.

C++
    
    
    LPCWSTR  IMTConSpread::MarginMaintenance()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConSpread.MarginMaintenance()

Python (Manager API)
    
    
    MTConSpread.MarginMaintenance

### Return Value

The value of the parameter for setting a maintenance margin.

# IMTConSpread::MarginMaintenance

Setting the value of the parameter for setting a maintenance margin.

C++
    
    
    MTAPIRES  IMTConSpread::MarginMaintenance(
       LPCWSTR  path      // The value for setting a maintenance margin
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.MarginMaintenance(
       string   path      // The value for setting a maintenance margin
       )

Python (Manager API)
    
    
    MTConSpread.MarginMaintenance

### Parameters

**path**  
[in] The value of the parameter for setting a maintenance margin.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

According to the margin charging type ([IMTConSpread:MarginType](MarginType.md)), different values are specified in this method:

  * MARGIN_TYPE_VALUE — the values of the maintenance margin that will be charged at the specified combination of positions;
  * MARGIN_TYPE_MAXIMAL — the value is not specified ([IMTConSpread::MarginMaintenance](MarginMaintenance.md) method is not used);
  * MARGIN_TYPE_CME_INTER — maintenance margin ratio (multiplier). The total margin value will be defined by summing up the margin requirements for all symbols of the spread (by [IMTConSymbol::MarginMaintenance](../../Symbols/IMTConSymbol/MarginInitial.md) value or the appropriate value redefined for [client group](../../Groups/IMTConGroupSymbol.md)) and multiplying the total value by the specified ratio;
  * MARGIN_TYPE_CME_INTRA — the difference between the total margin of A leg symbols and the total margin of B leg symbols is calculated (the difference in absolute magnitude is used, so that it does matter what leg is a deductible one). The value specified in [IMTConSpread::MarginMaintenance](MarginMaintenance.md) parameter is added to the obtained difference.


