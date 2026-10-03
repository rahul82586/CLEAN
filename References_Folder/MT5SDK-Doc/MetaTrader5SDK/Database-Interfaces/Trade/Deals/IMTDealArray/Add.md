[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTDealArray::Add

Add an object of a deal at the end of an array.

C++
    
    
    MTAPIRES  IMTDealArray::Add(
       IMTDeal*  deal      // A deal to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.Add(
       CIMTDeal  deal      // A deal to be added
       )

### Parameters

**deal**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the deal object is passed to the array object. Thus, when deleting an array object (call of [IMTDealArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTDealArray::Add

Add an object of the array of deals at the end of an array.

C++
    
    
    MTAPIRES  IMTDealArray::Add(
       IMTDealArray*  array      // An array of deals that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.Add(
       CIMTDealArray  array      // An array of deals that is being added
       )

### Parameters

**array**  
[in] An object of the array of deals.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTDealArray *array=api->DealCreateArray();   
       IMTDeal      *deal =api->DealCreate();
    //---
       array->Add(deal);   // After that the lifetime is controlled by an array
       array->Delete(0);   // Delete the first element, and the pointer in deal becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTDealArray  *array=api->DealCreateArray();   
       IMTDeal       *deal =api->DealCreate();
    //---
       array->Add(deal);
       array->Add(deal); // In this case the array will contain two pointers to one and the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
