[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerStart

[Previous](DealerUnsubscribe.md) | [Next](DealerStop.md)

# IMTManagerAPI::DealerStart

Start dealing.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerStart()

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerStart()

Python
    
    
    ManagerAPI.DealerStart()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

After the execution of this method, the queue of trade requests will be loaded to the application, and [events associated with trade requests](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestSink.md) (OnRequestAdd, OnRequestUpdate, OnRequestDelete and OnRequestSync) will start arriving.
