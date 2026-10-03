[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTDealArray::Delete

Delete an object of a deal by its position.

C++
    
    
    MTAPIRES  IMTDealArray::Delete(
       const UINT  pos      // Position of a deal
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.Delete(
       uint        pos      // Position of a deal
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The deleted object will be automatically released by calling the [IMTDeal::Release](../IMTDeal/Release.md) method.
