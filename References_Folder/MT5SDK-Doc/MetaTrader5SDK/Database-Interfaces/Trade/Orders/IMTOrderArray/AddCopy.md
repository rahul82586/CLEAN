[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTOrderArray::AddCopy

Add a copy of an object of a trade order at the end of an array.

C++
    
    
    MTAPIRES  IMTOrderArray::AddCopy(
       const IMTOrder*  order      // An order that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.AddCopy(
       CIMTOrder        order      // An order that is being added
       )

### Parameters

**order**  
[in] An object of a trading order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the order object and places it at the end of the array.

# IMTOrderArray::AddCopy

Add copies of the objects of trade orders in an array.

C++
    
    
    MTAPIRES  IMTOrderArray::AddCopy(
       const IMTOrderArray*  array      // An array of orders that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.AddCopy(
       CIMTOrderArray        array      // An array of orders that is being added
       )

### Parameters

**array**  
[in] An object of the array of trade orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the objects of trade orders belonging to the array object, and inserts them at the end of the current array.
