[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests Reason

[Previous](Requests-PositionByExternalID.md) | [Next](Requests-ApiDataSet.md)

# IMTRequest::Reason

Get the reason for creating the request.

C++
    
    
    UINT  IMTRequest::Reason()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTRequest.Reason()

### Return Value

A value from the [IMTOrder::EnOrderReason (#enorderreason)](../../Orders/IMTOrder/Enumerations.md#enorderreason) enumeration.

# IMTRequest::ReasonSet

Set the reason for creating the request.

C++
    
    
    MTAPIRES  IMTRequest::Reason(
       const UINT  reason    // reason
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.Reason(
       uint        reason    // reason
       )

### Parameters

**reason**  
[in] Reason for creating the request. The value is passed using theIMTOrder::EnOrderReasonenumeration.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.

### Note

Do not change request setting reasons unless absolutely necessary as this may violate the data integrity.
