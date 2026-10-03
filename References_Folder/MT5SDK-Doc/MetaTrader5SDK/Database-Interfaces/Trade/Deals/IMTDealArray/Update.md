[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTDealArray::Update

Changes a deal at the specified position of an array.

C++
    
    
    MTAPIRES  IMTDealArray::Update(
       const UINT  pos,      // Position
       IMTDeal*    deal      // An object of a deal
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDealArray.Update(
       uint        pos,      // Position
       CIMTDeal    deal      // An object of a deal
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

**deal**  
[in] An object of a deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTDealArray::Update method deletes the previous element (call of [IMTDeal::Release](../IMTDeal/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTDealArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTDealArray *array=api->DealCreateArray();   
       IMTDeal      *deal1=api->DealCreate();
       IMTDeal      *deal2=api->DealCreate();
    //---
       array->Add(deal1);
       array->Update(0,deal2); // The first element (object deal1) is replaced by deal2
       //--- After that the deal1 element will be released using Release, and the deal2 lifetime will be controlled by the array
