[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon LimitSymbols

[Previous](IMTCon-LimitGroups.md) | [Next](IMTCon-LiveUpdateMode.md)

# IMTConCommon::LimitSymbols

Get the maximum number of [financial instruments](../../Symbols.md) that can be created in the trading platform.

C++
    
    
    UINT  IMTConCommon::LimitSymbols()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConCommon.LimitSymbols()

Python (Manager API)
    
    
    MTConCommon.LimitSymbols

### Return value

The maximum number of symbols.

### Note

The maximum number of symbols is specified in the license.
