[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests AddCopy

[Previous](Requests-Add.md) | [Next](Requests-Delete.md)

# IMTRequestArray::AddCopy

Add a copy of an object of a trade request at the end of an array.

C++
    
    
    MTAPIRES  IMTRequestArray::AddCopy(
       const IMTRequest*  request      // Added request
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.AddCopy(
       CIMTRequest        request      // Added request
       )

### Parameters

**request**  
[in] An object of a trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the request object and places it at the end of the array.

# IMTRequestArray::AddCopy

Add copies of the objects of trade requests in an array.

C++
    
    
    MTAPIRES  IMTRequestArray::AddCopy(
       const IMTRequestArray*  array      // The array of requests that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.AddCopy(
       CIMTRequestArray        array      // The array of requests that is being added
       )

### Parameters

**array**  
[in] An object of the array of requests.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the objects of requests belonging to the array object, and inserts them at the end of the current array.
