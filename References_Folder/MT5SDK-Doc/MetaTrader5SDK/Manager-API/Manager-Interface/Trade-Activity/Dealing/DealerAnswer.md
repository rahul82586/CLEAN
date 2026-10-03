[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerAnswer

[Previous](DealerLock.md) | [Next](DealerSend.md)

# IMTManagerAPI::DealerAnswer

Respond to a trade request received for processing using the [IMTManagerAPI::DealerGet](DealerGet.md) or [IMTManagerAPI::DealerLock](DealerLock.md) method.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerAnswer(
       IMTConfirm*  confirm      // An objet of trade request confirmation
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerAnswer(
       CIMTConfirm  confirm      // An objet of trade request confirmation
       )

Python
    
    
    MTManagerAPI.DealerAnswer(
       confirm      # An objet of trade request confirmation
       )

### Parameters

**confirm**  
[in] Filledobject of the trade request confirmation.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method can be used only after calling [IMTManagerAPI::DealerStart](DealerStart.md).
