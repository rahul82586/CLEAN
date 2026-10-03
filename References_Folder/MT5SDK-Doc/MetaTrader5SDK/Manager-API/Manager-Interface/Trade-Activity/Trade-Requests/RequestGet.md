[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Trade Requests](../Trade-Requests.md) / RequestGet

[Previous](RequestNext.md) | [Next](RequestGetAll.md)

# IMTManagerAPI::RequestGet

Get a trade request by ID.

C++
    
    
    MTAPIRES  IMTManagerAPI::RequestGet(
       const UINT   id,          // Request ID
       IMTRequest*  request      // An object of a trade request
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.RequestGet(
       uint         id,          // Request ID
       CIMTRequest  request      // An object of a trade request
       )

Python
    
    
    ManagerAPI.RequestGet(
       id           # Request ID
       )

### Parameters

**id**  
[in] Trade request ID. TheIMTRequest::Idvalue is used as the identifier.

**request**  
[out] An object of a trade request. The request object must first be created using theIMTManagerAPI::RequestCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

To use this method, you must first call [IMTManagerAPI::DealerStart](../Dealing/DealerStart.md).
