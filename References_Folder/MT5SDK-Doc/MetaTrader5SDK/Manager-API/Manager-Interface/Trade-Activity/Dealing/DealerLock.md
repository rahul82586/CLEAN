[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerLock

[Previous](DealerGet.md) | [Next](DealerAnswer.md)

# IMTManagerAPI::DealerLock

Get a request with a specified ID for processing.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerLock(
       const UINT   id,          // Trade request ID
       IMTRequest*  request      // An object of a trade request
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerLock(
       uint         id,          // Trade request ID
       CIMTRequest  request      // An object of a trade request
       )

Python
    
    
    MTManagerAPI.DealerLock(
       id,          # Trade request ID
       )

### Parameters

**id**  
[in] Trade request ID. TheIMTRequest::Idvalue is used as the identifier.

**request**  
[out] An object of a trade request. The object must first be created using theIMTManagerAPI::RequestCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. Code MT_RET_OK_NONE means that the request is no longer available on the trade server. For example, it could have been captured by another dealer or application.

### Note

This method can be used only after calling [IMTManagerAPI::DealerStart](DealerStart.md).
