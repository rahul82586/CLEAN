[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTPositionArray::Add

Add an object of a trade position at the end of an array.

C++
    
    
    MTAPIRES  IMTPositionArray::Add(
       IMTPosition*  position      // The position that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.Add(
       CIMTPosition  position      // The position that is being added
       )

### Parameters

**position**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the position object is passed to the array object. Thus, when deleting an array object (call of [IMTPositionArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTPositionArray::Add

Add an object of the array of trade positions at the end of an array.

C++
    
    
    MTAPIRES  IMTPositionArray::Add(
       IMTPositionArray*  array      // The array of positions that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.Add(
       CIMTPositionArray  array      // The array of positions that is being added
       )

### Parameters

**array**  
[in] An object of the array of positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTPositionArray *array   =api->PositionCreateArray();   
       IMTPosition      *position=api->PositionCreate();
    //---
       array->Add(position);// After that the lifetime is controlled by the array
       array->Delete(0);    // Delete the first element, and the pointer in position becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTPositionArray  *array   =api->PositionCreateArray();   
       IMTPosition       *position=api->PositionCreate();
    //---
       array->Add(position);
       array->Add(position); // In this case the array contains two pointers to the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
