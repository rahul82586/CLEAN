[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTDealArray::UpdateCopy

Change a deal at the specified position of an array by copying the parameters of a passed object of a deal.

C++
    
    
    MTAPIRES  IMTDealArray::UpdateCopy(
       const UINT       pos,       // Position
       const IMTDeal*   deal       // An object of a deal
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.UpdateCopy(
       uint             pos,       // Position
       CIMTDeal         deal       // An object of a deal
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

**order**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the deal object into an object of a deal at the specified position of an array.

Unlike the [IMTDealArray::Update](Update.md) method, calling this method does not set any additional conditions for the control of the deal object, but is more resource-intensive, since an additional object is created.
