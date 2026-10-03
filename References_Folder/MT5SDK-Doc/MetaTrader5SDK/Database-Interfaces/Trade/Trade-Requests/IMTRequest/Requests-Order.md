[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Order

[Previous](Requests-VolumeCurrentExt.md) | [Next](Requests-OrderExternalID.md)

# IMTRequest::Order

Get the ticket of an order in a trade request.

C++
    
    
    UINT64  IMTRequest::Order()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTRequest.Order()

### Return Value

The ticket of an order in a trade request.

# IMTRequest::Order

Set the ticket of an order in a trade request.

C++
    
    
    MTAPIRES  IMTRequest::Order(
       const UINT64  order      // Order ticket
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Order(
       ulong         order      // Order ticket
       )

### Parameters

**order**  
[in] The ticket of an order in a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
