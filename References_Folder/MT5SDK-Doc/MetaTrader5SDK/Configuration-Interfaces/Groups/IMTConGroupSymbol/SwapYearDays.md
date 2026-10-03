[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SwapYearDays

[Previous](Swap3DayDefault.md) | [Next](SwapYearDaysDefault.md)

# IMTConGroupSymbol::SwapYearDays

Get the number of days in a year used in calculating [swap percent (#percentage)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps#percentage) for a given group.

C++
    
    
    UINT  IMTConGroupSymbol::SwapYearDays()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroupSymbol.SwapYearDays()

Python (Manager API)
    
    
    MTConGroupSymbol.SwapYearDays

### Return Value

The number of days in a year.

# IMTConGroupSymbol::SwapYearDays

Set the number of days in a year used in calculating [swap percent (#percentage)](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps#percentage) for a given group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SwapYearDays(
       const UINT  days     // Number of days
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SwapYearDays(
       uint        days     // Number of days
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SwapYearDays

### Parameters

**days**  
[in] Number of days in a year.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a relevant error code is returned.
