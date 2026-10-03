[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTOrder::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTOrder::Assign(
       const IMTOrder*  order      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.Assign(
       CIMTOrder        order      // Source object
       )

### Parameters

**order**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
