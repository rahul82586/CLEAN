[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTDealArray::AddCopy

Add a copy of an object of a deal at the end of an array.

C++
    
    
    MTAPIRES  IMTDealArray::AddCopy(
       const IMTDeal*  deal      // A deal to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.AddCopy(
       CIMTDeal        deal      // A deal to be added
       )

### Parameters

**deal**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the deal object and places it at the end of the array.

# IMTDealArray::AddCopy

Add copies of deal objects into an array.

C++
    
    
    MTAPIRES  IMTDealArray::AddCopy(
       const IMTDealArray*  array      // An array of deals that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.AddCopy(
       CIMTDealArray        array      // An array of deals that is being added
       )

### Parameters

**array**  
[in] An object of the array of deals.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the objects of deals belonging to the array object, and inserts them at the end of the current array.
