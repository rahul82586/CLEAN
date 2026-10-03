[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / SpreadDiffBalance

[Previous](SpreadDiffDefault.md) | [Next](SpreadDiffBalanceDefault.md)

# IMTConGroupSymbol::SpreadDiffBalance

Gets the balance of the spread difference for the group ([IMTConGroupSymbols::SpreadDiff)](SpreadDiff.md).

C++
    
    
    INT  IMTConGroupSymbol::SpreadDiffBalance()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConGroupSymbol.SpreadDiffBalance()

Python (Manager API)
    
    
    MTConGroupSymbol.SpreadDiffBalance

### Return Value

Balance of spread difference.

### Note

The value of the spread difference balance is defined as an offset from the equal division of the spread difference value ([IMTConGroupSymbol::SpreadDiff)](SpreadDiff.md) between the Bid and Ask prices. For example, if the spread difference is 4, its distribution in the ratio of -2 Bid/+2 Ask is equal to the spread difference balance value of 0. Ratio -3 Bid/+1 Ask corresponds to -1, ratio -1 Bid/+3 Ask corresponds to 1. If the spread difference value is odd, the 0 value of the spread difference value corresponds to its even distribution between the Bid and Ask prices with an offset of 1 in the Bid price direction. For example, if the spread difference is 3, the zero spread balance corresponds to the ratio -2 Bid/+1 Ask. 

  * New Bid = Bid - Point*((SpreadDiff+1)/2 - SpreadDiffBalance).
  * New Ask = Ask + Point*(SpreadDiff/2 + SpreadDiffBalance).



# IMTConGroupSymbol::SpreadDiffBalance

Sets the balance of the spread difference for the group ([IMTConGroupSymbols::SpreadDiff)](SpreadDiff.md).

C++
    
    
    MTAPIRES  IMTConGroupSymbol::SpreadDiffBalance(
       const INT  spread      // Spread difference balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.SpreadDiffBalance(
       const INT  spread      // Spread difference balance
       )

Python (Manager API)
    
    
    MTConGroupSymbol.SpreadDiffBalance

### Parameters

**spread**  
[in] Spread difference balance

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The value of the spread difference balance is defined as an offset from the equal division of the spread difference value ([IMTConGroupSymbol::SpreadDiff)](SpreadDiff.md) between the Bid and Ask prices. For example, if the spread difference is 4, its distribution in the ratio of -2 Bid/+2 Ask is equal to the spread difference balance value of 0. Ratio -3 Bid/+1 Ask corresponds to -1, ratio -1 Bid/+3 Ask corresponds to 1. If the spread difference value is odd, the 0 value of the spread difference value corresponds to its even distribution between the Bid and Ask prices with an offset of 1 in the Bid price direction. For example, if the spread difference is 3, the zero spread balance corresponds to the ratio -2 Bid/+1 Ask. 

  * New Bid = Bid - Point*((SpreadDiff+1)/2 - SpreadDiffBalance).
  * New Ask = Ask + Point*(SpreadDiff/2 + SpreadDiffBalance).


