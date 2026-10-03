[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / SpreadDiffBalance

[Previous](SpreadDiff.md) | [Next](TickValue.md)

# IMTConSymbol::SpreadDiffBalance

Get the balance of spread difference.

C++
    
    
    INT  IMTConSymbol::SpreadDiffBalance()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConSymbol.SpreadDiffBalance()

Python (Manager API)
    
    
    MTConSymbol.SpreadDiffBalance

### Return Value

Balance of spread difference. This parameter is used to set individual spread balance values ​​for certain groups of clients.

### Note

This method returns the base value of the balance of spread difference, which is actually equal to 0. To work with the balance of spread difference of a certain group, the [IMTConGroupSymbol::SpreadDiffBalance](../../Groups/IMTConGroupSymbol/SpreadDiffBalance.md) method should be used.

  * New Bid = Bid - Point*((SpreadDiff+1)/2 - SpreadDiffBalance).
  * New Ask = Ask + Point*(SpreadDiff/2 + SpreadDiffBalance).



# IMTConSymbol::SpreadDiffBalance

Set the balance of spread difference.

C++
    
    
    MTAPIRES  IMTConSymbol::SpreadDiffBalance(
       const INT  spread      // Spread difference balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.SpreadDiffBalance(
       int        spread      // Spread difference balance
       )

Python (Manager API)
    
    
    MTConSymbol.SpreadDiffBalance

### Parameters

**spread**  
[in] Spread difference balance

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method sets the base value of the balance of spread difference. To set the individual spread balance value for certain groups of clients, the [IMTConGroupSymbol::SpreadDiffBalance](../../Groups/IMTConGroupSymbol/SpreadDiffBalance.md) method is used.

  * New Bid = Bid - Point*((SpreadDiff+1)/2 - SpreadDiffBalance).
  * New Ask = Ask + Point*(SpreadDiff/2 + SpreadDiffBalance).


