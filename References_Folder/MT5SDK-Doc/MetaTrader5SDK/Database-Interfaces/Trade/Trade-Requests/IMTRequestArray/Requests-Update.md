[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Update

[Previous](Requests-Detach.md) | [Next](Requests-UpdateCopy.md)

# IMTRequestArray::Update

Change a trade request at the specified position of an array.

C++
    
    
    MTAPIRES  IMTRequestArray::Update(
       const UINT   pos,         // Request position
       IMTRequest*  request      // Request object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequestArray.Update(
       uint         pos,         // Request position
       CIMTRequest  request      // Request object
       )

### Parameters

**pos**  
[in] Position of a trade request in an array, starting with 0.

**request**  
[in] An object of a request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTRequestArray::Update method deletes the previous element (call of [IMTRequest::Release](../IMTRequest/Requests-Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTRequestArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTRequestArray *array   =api->RequestArrayCreate();   
       IMTRequest      *request1=api->RequestCreate();
       IMTRequest      *request2=api->RequestCreate();
    //---
       array->Add(request1);
       array->Update(0,request2); // The first element (object request1) is replaced by request2
       //--- After that the request1 element will be released using Release, and the request2 lifetime will be controlled by the array
