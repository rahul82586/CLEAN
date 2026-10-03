[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Trade Requests](../Trade-Requests.md) / RequestGetAll

[Previous](RequestGet.md) | [Next](../Auxiliary-Functions.md)

# IMTManagerAPI::RequestGetAll

Get all the trade requests in a queue.

C++
    
    
    MTAPIRES  IMTManagerAPI::RequestGetAll(
       IMTRequestArray*  requests      // An object of the array of requests
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.RequestGetAll(
       CIMTRequestArray  requests      // An object of the array of requests
       )

Python
    
    
    ManagerAPI.RequestGetAll(
       requests          # An object of the array of requests
       )

### Parameters

**requests**  
[out] An object of the array of requests. The requests object must first be created using theIMTManagerAPI::RequestCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the array of trade requests in a queue to the requests object. To use this method, you must first call [IMTManagerAPI::DealerStart](../Dealing/DealerStart.md).
