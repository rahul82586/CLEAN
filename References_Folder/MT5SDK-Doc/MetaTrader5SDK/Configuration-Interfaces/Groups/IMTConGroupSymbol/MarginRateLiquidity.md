[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginRateLiquidity

[Previous](MarginRateMaintenanceDefault.md) | [Next](MarginRateLiquidityDefault.md)

# IMTConGroupSymbol::MarginRateLiquidity

Gets symbol liquidity rate for this group. The liquidity margin rate determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).

C++
    
    
    double  IMTConGroupSymbol::MarginRateLiquidity()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginRateLiquidity()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateLiquidity

### Return Value

The liquidity rate of a symbol.

# IMTConGroupSymbol::MarginRateLiquidity

Sets symbol liquidity rate for this group. The liquidity margin rate determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).

C++
    
    
    MTAPIRES  IMTConGroupSymbol::MarginRateLiquidity(
       const double  margin_rate // Liquidity rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.MarginRateLiquidity(
       double        margin_rate // Liquidity rate
       )

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateLiquidity

### Parameters

**margin_rate**  
[in] Symbol liquidity rate.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
