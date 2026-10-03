[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Action

[Previous](Requests-DigitsSet.md) | [Next](Requests-TimeExpiration.md)

# IMTRequest::Action

Get the type of action to which the trade request belongs.

C++
    
    
    UINT  IMTRequest::Action()  const

.NET (Gateway/Manager API)
    
    
    EnTradeActions  CIMTRequest.Action()

### Return Value

A value of the [IMTRequest::EnTradeActions (#entradeactions)](Requests-Enumerations.md#entradeactions) enumeration.

# IMTRequest::Action

Set the type of action to which the trade request belongs.

C++
    
    
    MTAPIRES  IMTRequest::Action(
       const UINT      action  // Action type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Action(
       EnTradeActions  action  // Action type
       )

### Parameters

**action**  
[in] The type of action. TheIMTRequest::EnTradeActionsenumeration is used to pass the type.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
