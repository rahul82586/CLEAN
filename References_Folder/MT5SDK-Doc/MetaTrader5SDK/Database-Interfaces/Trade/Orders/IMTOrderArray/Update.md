[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTOrderArray::Update

Changes an order at the specified position of an array.

C++
    
    
    MTAPIRES  IMTOrderArray::Update(
       const UINT  pos,       // Position
       IMTOrder*   order      // An object of a trade order
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Update(
       uint        pos,       // Position
       CIMTOrder   order      // An object of a trade order
       )

### Parameters

**pos**  
[in] Position of an order in an array, starting with 0.

**order**  
[in] An object of a trading order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTOrderArray::Update method deletes the previous element (call of [IMTOrder::Release](../IMTOrder/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTOrderArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTOrderArray *array =api->OrderCreateArray();   
       IMTOrder      *order1=api->OrderCreate();
       IMTOrder      *order2=api->OrderCreate();
    //---
       array->Add(order1);
       array->Update(0,order2); // The first element (object order1) is replaced by order2
       //--- After that the order1 element will be released using Release, and the order2 lifetime will be controlled by the array
