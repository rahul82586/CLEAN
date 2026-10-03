[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTOrderArray::Add

Add an object of a trade order at the end of an array.

C++
    
    
    MTAPIRES  IMTOrderArray::Add(
       IMTOrder*  order      // An order that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Add(
       CIMTOrder  order      // An order that is being added
       )

### Parameters

**order**  
[in] An object of a trading order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the order object is passed to the array object. Thus, when deleting an array object (call of [IMTOrderArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTOrderArray::Add

Add an object of the array of orders at the end of an array.

C++
    
    
    MTAPIRES  IMTOrderArray::Add(
       IMTOrderArray*  array      // An array of orders that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrderArray.Add(
       CIMTOrderArray  array      // An array of orders that is being added
       )

### Parameters

**array**  
[in] An object of the array of trade orders.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTOrderArray *array=api->OrderCreateArray();   
       IMTOrder      *order=api->OrderCreate();
    //---
       array->Add(order);  // After that the lifetime is controlled by an array
       array->Delete(0);   // Delete the first element, and the pointer in order becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTOrderArray  *array=api->OrderCreateArray();   
       IMTOrder       *order=api->OrderCreate();
    //---
       array->Add(order);
       array->Add(order); // In this case the array contains two pointers to the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
