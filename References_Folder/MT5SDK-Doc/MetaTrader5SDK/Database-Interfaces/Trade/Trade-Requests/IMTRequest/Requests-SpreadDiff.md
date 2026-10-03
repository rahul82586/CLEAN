[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests SpreadDiff

[Previous](Requests-PriceDeviationBottom.md) | [Next](Requests-SpreadDiffBalance.md)

# IMTRequest::SpreadDiff

Get the difference between the symbol spread for the group to which the trader belongs and the current symbol spread (price markup for the group).

C++
    
    
    INT  IMTRequest::SpreadDiff()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTRequest.SpreadDiff()

### Return Value

Symbol spread difference.

### Note

The server copies the value from the settings specified in the trader group ([IMTConGroupSymbols::SpreadDiff](../../../../Configuration-Interfaces/Groups/IMTConGroupSymbol/SpreadDiff.md)) at the time the request is formed. You can use this property when forwarding requests to the exchange via the Gateway API, to inform the exchange about the platform-side price markup if such information is required by the exchange rules.

# IMTRequest::SpreadDiff

Set the difference between the symbol spread for the group to which the trader belongs and the current symbol spread.

C++
    
    
    MTAPIRES  IMTRequest::SpreadDiff(
       const INT  spread      // spread difference
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.SpreadDiff(
       int        spread      // spread difference
       )

### Parameters

**spread**  
[in] Symbol spread difference.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Do not change the value of this property unless absolutely necessary. It is only used to notify the exchange about the platform-side price difference value.
