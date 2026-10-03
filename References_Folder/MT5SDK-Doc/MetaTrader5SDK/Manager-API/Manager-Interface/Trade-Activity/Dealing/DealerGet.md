[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerGet

[Previous](DealerStop.md) | [Next](DealerLock.md)

# IMTManagerAPI::DealerGet

Get the first request in the queue of requests for processing.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerGet(
       IMTRequest*  request      // An object of a trade request
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerGet(
       CIMTRequest  request      // An object of a trade request
       )

Python
    
    
    MTManagerAPI.DealerGet()

### Parameters

**request**  
[out] An object of a trade request. The object must first be created using theIMTManagerAPI::RequestCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method can be used only after calling [IMTManagerAPI::DealerStart](DealerStart.md).
