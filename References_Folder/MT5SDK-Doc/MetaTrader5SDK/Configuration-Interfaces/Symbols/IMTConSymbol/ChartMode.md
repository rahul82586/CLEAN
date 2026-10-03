[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / ChartMode

[Previous](SpliceTimeDays.md) | [Next](OptionsMode.md)

# IMTConSymbol::ChartMode

Getting the chart creation mode for the symbol.

C++
    
    
    UINT  IMTConSymbol::ChartMode()  const

.NET (Gateway/Manager API)
    
    
    EnChartMode  CIMTConSymbol.ChartMode()

Python (Manager API)
    
    
    MTConSymbol.ChartMode

### Return Value

One of the values of the [IMTConSymbol::EnChartMode (#enchartmode)](Enumerations.md#enchartmode) enumeration.

# IMTConSymbol::ChartMode

Setting the chart creation mode for the symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::ChartMode(
       const UINT  mode      // Charting mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.ChartMode(
       EnChartMode mode      // Charting mode
       )

Python (Manager API)
    
    
    MTConSymbol.ChartMode

### Parameters

**mode**  
[in] To pass the chart drawing mode, theIMTConSymbol::EnChartModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Further Note

When you change the chart drawing mode, the accumulated price history will not be changed. Settings only apply to new received data.
