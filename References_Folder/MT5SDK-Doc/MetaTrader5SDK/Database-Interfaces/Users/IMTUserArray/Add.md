[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTUserArray::Add

Adds a client record object at the end of an array.

C++
    
    
    MTAPIRES  IMTUserArray::Add(
       IMTUser*  user      // The client record to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.Add(
       CIMTUser  user      // The client record to be added
       )

### Parameters

**user**  
[in] An object of the client record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the user object is passed to the array object. Thus, when deleting an array object (call of [IMTUserArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTUserArray::Add

Adds an object client records array at the end of an array.

C++
    
    
    MTAPIRES  IMTUserArray::Add(
       IMTUserArray*  array      // An array of client records to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.Add(
       CIMTUserArray  array      // An array of client records to be added
       )

### Parameters

**array**  
[in] An object of arrays of client records.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTUserArray *array=api->UserCreateArray();   
       IMTUser      *user=api->UserCreate();
    //---
       array->Add(user);   // After that the lifetime is controlled by an array
       array->Delete(0);   // Delete the first element, and the pointer in order becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTUserArray  *array=api->UserCreateArray();   
       IMTUser       *usero=api->UserCreate();
    //---
       array->Add(user);
       array->Add(user); // In this case the array contains two pointers to the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
