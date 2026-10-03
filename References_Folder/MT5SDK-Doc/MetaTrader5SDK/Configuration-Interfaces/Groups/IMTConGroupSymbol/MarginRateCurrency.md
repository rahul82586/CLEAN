[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginRateCurrency

[Previous](MarginRateLiquidityDefault.md) | [Next](MarginRateCurrencyDefault.md)

# IMTConGroupSymbol::MarginRateCurrency

Get the margin currency rate for this group.

C++
    
    
    double  IMTConGroupSymbol::MarginRateCurrency()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginRateCurrency()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateCurrency

### Return Value

Currency margin rate.

### Note

Margin currency rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#encalcmode)](../../Symbols/IMTConSymbol/Enumerations.md#encalcmode)) traded on Moscow Exchange (calculating variation margin and security deposit using the current USD exchange rate). The values are sent by the Moscow Exchange when using the gateway MetaTrader 5 to MOEX Derivatives.

# IMTConGroupSymbol::MarginRateCurrency

Set the margin currency rate for this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginRateCurrency(
       const double  margin_rate  // Margin currency rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginRateCurrency(
       double        margin_rate  // Margin currency rate
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateCurrency

### Parameters

**margin**  
[in] Margin currency rate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Margin currency rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#encalcmode)](../../Symbols/IMTConSymbol/Enumerations.md#encalcmode)) traded on Moscow Exchange (calculating variation margin and security deposit using the current USD exchange rate). The values are sent by the Moscow Exchange when using the gateway MetaTrader 5 to MOEX Derivatives.
