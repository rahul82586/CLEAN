[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / MarginRateLiquidityDefault

[Previous](MarginRateLiquidity.md) | [Next](MarginRateCurrency.md)

# IMTConGroupSymbol::MarginRateLiquidityDefault

Gets the default liquidity rate of the symbol. For a more detailed description, please read the ["Use of Default method" (#default)](../IMTConGroupSymbol.md#default) section.

C++
    
    
    double  IMTConGroupSymbol::MarginRateLiquidityDefault()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroupSymbol.MarginRateLiquidityDefault()

Python (Manager API)
    
    
    MTConGroupSymbol.MarginRateLiquidityDefault

### Note

The liquidity margin rate determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity).
