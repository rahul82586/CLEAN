[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SpreadBalance

[Previous](Spread.md) | [Next](SpreadDiff.md)

# IMTConSymbol::SpreadBalance

Get the spread balance of a symbol.

C++
    
    
    INT  IMTConSymbol::SpreadBalance()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConSymbol.SpreadBalance()

Python (Manager API)
    
    
    MTConSymbol.SpreadBalance

### Return Value

Symbol spread balance.

### Note

Spread balance is set a shift from the equal distribution of the spread value ([IMTConSymbol::Spread](Spread.md)) between Bid and Ask prices. For example, if the spread is 10, its distribution in the ratio of -5 Bid/+ 5 Ask is equal to the spread balance value of 0. Ratio -6 Bid/+4 Ask corresponds to -1, ratio -4 Bid/+6 Ask corresponds to 1. If the spread value is odd, the 0 value of the spread value corresponds to its even distribution between the Bid and Ask prices with an offset of 1 in the Ask direction. For example, if the spread is 3, the zero spread balance corresponds to the ratio -1 Bid/+2 Ask. 

  * If the spread of incoming quotes is equal to the spread specified for the symbol, then the prices are transformed according to the following formula: New Bid = Bid + Points * Spread Balance, where Points is the point size ([IMTConSymbol::Point](Point.md)). News Ask = News Bid + Spread.
  * If the spread of incoming quotes differs from the spread specified for the symbol, then the prices are transformed according to the following formula: New Bid = (Ask + Bid)/2 - Points * (Spread/2 - Spread Balance), where Points is the point size ([IMTConSymbol::Point](Point.md)). News Ask = News Bid + Spread.
  * If floating spread (0) is set for the symbol, prices are shifted by the same Spread Balance value.



# IMTConSymbol::SpreadBalance

Set the spread balance of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbol::SpreadBalance(
       const INT  spread      // Spread balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SpreadBalance(
       int        spread      // Spread balance
       )

Python (Manager API)
    
    
    MTConSymbol.SpreadBalance

### Parameters

**spread**  
[in] The symbol spread balance.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Spread balance is set a shift from the equal distribution of the [spread ](Spread.md)value between Bid and Ask prices. For example, if the spread is 10, its distribution in the ratio of -5 Bid/+ 5 Ask is equal to the spread balance value of 0. Ratio -6 Bid/+4 Ask corresponds to -1, ratio -4 Bid/+6 Ask corresponds to 1. If the spread value is odd, the 0 value of the spread value corresponds to its even distribution between the Bid and Ask prices with an offset of 1 in the Ask direction. For example, if the spread is 3, the 0 spread balance corresponds to the distribution -1 Bid/+2 Ask.

  * If the spread of incoming quotes is equal to the spread specified for the symbol, then the prices are transformed according to the following formula: New Bid = Bid + Points * Spread Balance, where Points is the point size ([IMTConSymbol::Point](Point.md)). News Ask = News Bid + Spread.
  * If the spread of incoming quotes differs from the spread specified for the symbol, then the prices are transformed according to the following formula: New Bid = (Ask + Bid)/2 - Points * (Spread/2 - Spread Balance), where Points is the point size ([IMTConSymbol::Point](Point.md)). News Ask = News Bid + Spread.
  * If floating spread (0) is set for the symbol, prices are shifted by the same Spread Balance value.


