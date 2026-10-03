[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests SpreadDiffBalance

[Previous](Requests-SpreadDiff.md) | [Next](Requests-Comment.md)

# IMTRequest::SpreadDiffBalance

Get the spread difference balance specified for the trader group.

C++
    
    
    INT  IMTRequest::SpreadDiffBalance()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTRequest.SpreadDiffBalance()

### Return Value

Spread difference balance.

### Note

The server copies the value from the settings specified in the trader group ([IMTConGroupSymbols::SpreadDiffBalance](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiffBalance.md)) at the time the request is formed. You can use this property when forwarding requests to the exchange via the Gateway API, to inform the exchange about the platform-side price markup if such information is required by the exchange rules.

  * New Bid = Bid - Point*((SpreadDiff+1)/2 - SpreadDiffBalance).
  * New Ask = Ask + Point*(SpreadDiff/2 + SpreadDiffBalance).



# IMTRequest::SpreadDiffBalance

Set the spread difference balance in a trade request.

C++
    
    
    MTAPIRES  IMTRequest::SpreadDiffBalance(
       const INT  spread      // spread difference balance
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.SpreadDiffBalance(
       const INT  spread      // spread difference balance
       )

### Parameters

**spread**  
[in] Spread difference balance.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Do not change the value of this property unless absolutely necessary. It is only used to notify the exchange about the platform-side price difference value.
