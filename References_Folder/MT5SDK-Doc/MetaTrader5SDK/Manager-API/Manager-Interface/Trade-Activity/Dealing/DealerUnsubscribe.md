[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerUnsubscribe

[Previous](DealerConfirmCreate.md) | [Next](DealerStart.md)

# IMTManagerAPI::DealerUnsubscribe

Unsubscribe from waiting for results of trading operations executed by [IMTManagerAPI::DealerSend](DealerSend.md) commands (by any manager).

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerUnsubscribe(
       IMTDealerSink*  sink      // A pointer to the IMTDealerSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerUnsubscribe(
       CIMTDealerSink  sink      // CIMTDealerSink object
       )

Python
    
    
    ManagerAPI.DealerUnsubscribe(
       sink            # MTDealerSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTDealerSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
