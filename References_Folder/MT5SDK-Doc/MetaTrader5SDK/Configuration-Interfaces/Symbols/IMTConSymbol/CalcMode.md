[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / CalcMode

[Previous](TradeMode.md) | [Next](ExecMode.md)

# IMTConSymbol::CalcMode

Get the current mode of margin and profit calculation.

C++
    
    
    UINT  IMTConSymbol::CalcMode()  const

.NET (Gateway/Manager API)
    
    
    EnCalcMode  CIMTConSymbol.CalcMode()

Python (Manager API)
    
    
    MTConSymbol.CalcMode

### Return Value

A value of the [IMTConSymbol::EnCalcMode (#encalcmode)](Enumerations.md#encalcmode) enumeration.

# IMTConSymbol::CalcMode

Set the mode of margin and profit calculation.

C++
    
    
    MTAPIRES  IMTConSymbol::CalcMode(
       const UINT  mode      // Margin and profit calculation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.CalcMode(
       EnCalcMode  mode      // Margin and profit calculation mode
       )

Python (Manager API)
    
    
    MTConSymbol.CalcMode

### Parameters

**mode**  
[in] To pass the margin and profit calculation mode, theIMTConSymbol::EnCalcModeenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
