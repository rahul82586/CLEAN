[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / MarginRateCurrency

[Previous](MarginHedged.md) | [Next](MarginRateLiquidity.md)

# IMTConSymbol::MarginRateCurrency

Get the margin currency rate.

C++
    
    
    double  IMTConSymbol::MarginRateCurrency()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConSymbol.MarginRateCurrency()

Python (Manager API)
    
    
    MTConSymbol.MarginRateCurrency

### Return Value

Currency margin rate.

### Note

Margin currency rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#encalcmode)](Enumerations.md#encalcmode)) traded on Moscow Exchange (calculating variation margin and security deposit using the current USD exchange rate). The values are sent by the Moscow Exchange when using the gateway MetaTrader 5 to MOEX Derivatives.

# IMTConSymbol::MarginRateCurrency

Set the margin currency rate.

C++
    
    
    MTAPIRES  IMTConSymbol::MarginRateCurrency(
       const double  margin_rate  // Margin currency rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.MarginRateCurrency(
       double        margin_rate  // Margin currency rate
       )

Python (Manager API)
    
    
    MTConSymbol.MarginRateCurrency

### Parameters

**margin**  
[in] Margin currency rate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Margin currency rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures (#encalcmode)](Enumerations.md#encalcmode)) traded on Moscow Exchange (calculating variation margin and security deposit using the current USD exchange rate). The values are sent by the Moscow Exchange when using the gateway MetaTrader 5 to MOEX Derivatives.
