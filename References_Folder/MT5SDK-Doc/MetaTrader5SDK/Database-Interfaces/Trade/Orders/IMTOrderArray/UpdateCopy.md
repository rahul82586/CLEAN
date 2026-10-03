[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTOrderArray::UpdateCopy

Change an order at the specified position of an array by copying the parameters of a passed object of an order.

C++
    
    
    MTAPIRES  IMTOrderArray::UpdateCopy(
       const UINT        pos,       // Position
       const IMTOrder*   order      // An object of a trade order
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.UpdateCopy(
       uint              pos,       // Position
       CIMTOrder         order      // An object of a trade order
       )

### Parameters

**pos**  
[in] Position of an order in an array, starting with 0.

**order**  
[in] An object of a trading order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the parameters of the order object into an object of an order at the specified position of an array.
