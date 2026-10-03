[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Flags

[Previous](Requests-TypeTime.md) | [Next](Requests-Volume.md)

# IMTRequest::Flags

Get additional flags of a trade request.

C++
    
    
    UINT  IMTRequest::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnTradeActionFlags  CIMTRequest.Flags()

### Return Value

A value of the [IMTRequest::EnTradeActionFlags (#entradeactionflags)](Requests-Enumerations.md#entradeactionflags) enumeration.

# IMTRequest::Flags

Set additional flags of a trade request.

C++
    
    
    MTAPIRES  IMTRequest::Flags(
       const UINT          flags  // Additional flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Flags(
       EnTradeActionFlags  flags  // Additional flags
       )

### Parameters

**flags**  
[in] TheIMTRequest::EnTradeActionFlagsenumeration is used for passing additional flags.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
