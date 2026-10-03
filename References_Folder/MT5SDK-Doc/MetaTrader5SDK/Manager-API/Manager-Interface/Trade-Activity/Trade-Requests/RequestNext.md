[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Trade Requests](../Trade-Requests.md) / RequestNext

[Previous](RequestTotal.md) | [Next](RequestGet.md)

# IMTManagerAPI::RequestNext

Get a trade request by a queue position.

C++
    
    
    MTAPIRES  IMTManagerAPI::RequestNext(
       const UINT   pos,         // Trade request position
       IMTRequest*  request      // An object of a trade request
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.RequestNext(
       uint         pos,         // Trade request position
       CIMTRequest  request      // An object of a trade request
       )

Python
    
    
    ManagerAPI.RequestNext(
       pos          # Trade request position
       )

### Parameters

**pos**  
[in] Position of a trade request in a queue, starting with 0.

**request**  
[out] An object of a trade request. The request object must first be created using theIMTManagerAPI::RequestCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies trade request data at the specified queue position to the request object. To use this method, you must first call [DealerStart](../Dealing/DealerStart.md).
