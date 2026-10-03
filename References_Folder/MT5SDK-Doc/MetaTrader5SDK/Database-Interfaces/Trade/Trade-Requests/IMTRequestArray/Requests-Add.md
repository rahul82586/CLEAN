[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Add

[Previous](Requests-Clear.md) | [Next](Requests-AddCopy.md)

# IMTRequestArray::Add

Add an object of a trade request at the end of an array.

C++
    
    
    MTAPIRES  IMTRequestArray::Add(
       IMTRequest*  request      // Added request
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.Add(
       CIMTRequest  request      // Added request
       )

### Parameters

**request**  
[in] An object of a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the request object is passed to the array object. Thus, when deleting an array object (call of [IMTRequestArray::Release](Requests-Release.md)), an earlier inserted object is automatically removed.

# IMTRequestArray::Add

Adds an object of the array of trade requests at the end of an array.

C++
    
    
    MTAPIRES  IMTRequestArray::Add(
       IMTRequestArray*  array      // The array of requests that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.Add(
       CIMTRequestArray  array      // The array of requests that is being added
       )

### Parameters

**array**  
[in] An object of the array of requests.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTRequestArray *array  =api->RequestCreateArray();   
       IMTRequest      *request=api->RequestCreate();
    //---
       array->Add(request); // After that the lifetime is controlled by the array
       array->Delete(0);    // Delete the first element, and the pointer in request becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTRequestArray  *array  =api->RequestCreateArray();   
       IMTRequest       *request=api->RequestCreate();
    //---
       array->Add(request);
       array->Add(request); // In this case the array contains two pointers to the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
