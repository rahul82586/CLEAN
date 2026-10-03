[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Update

[Previous](IMTHistoryDealArray-Detach.md) | [Next](IMTHistoryDealArray-UpdateCopy.md)

# IMTECNHistoryDealArray::Update

Change a deal at the specified position of an array.

C++
    
    
    MTAPIRES  IMTECNHistoryDealArray::Update(
       const UINT              pos,    // position
       IMTECNHistoryDeal*      deal    // deal object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDealArray.Update(
       uint                    pos,    // position
       CIMTECNHistoryDealArray      deal    // deal object
       )

### Parameters

**pos**  
[in] Position of a deal in an array, starting with 0.

**deal**  
[in]Deal object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The IMTECNHistoryDealArray::Update method deletes the previous element ([IMTECNHistoryDealArray::Release](../IMTECNMatching/IMTMatching-Release.md) call) and replaces it with a new one. After that, the lifetime of the new element is controlled by an array object. Thus, when deleting an array object (by IMTECNHistoryDealArray::Release call), the earlier inserted objects will be automatically deleted.

### Example
    
    
    //--- example
      IMTECNHistoryDealArray *array=api->ECNHistoryDealCreateArray();  
      IMTECNHistoryDeal      *deal1=api->ECNHistoryDealCreate();
      IMTECNHistoryDeal      *deal2=api->ECNHistoryDealCreate();
    //---
       array->Add(order1);
       array->Update(0,order2); // the first element (the deal1 object) is replaced with deal2
       //--- after that the deal1 element will be released via Release, and deal2 lifetime will be controlled by the array
