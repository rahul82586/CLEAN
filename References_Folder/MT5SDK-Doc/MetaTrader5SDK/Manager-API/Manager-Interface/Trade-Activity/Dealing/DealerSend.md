[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Dealing](../Dealing.md) / DealerSend

[Previous](DealerAnswer.md) | [Next](DealerBalance.md)

# IMTManagerAPI::DealerSend

Send a trade request to the server.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealerSend(
       IMTRequest*    request,     // An object of a trade request
       IMTDealerSink* sink,        // A pointer to the IMTDealerSink object
       UINT&          id           // Request ID
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealerSend(
       CIMTRequest    request,     // An object of a trade request
       CIMTDealerSink sink,        // CIMTDealerSink object
       out uint       id           // Request ID
       )

Python
    
    
    ManagerAPI.DealerSend(
       request,       # объект торгового запроса
       sink           # MTDealerSink object
       )

### Parameters

**request**  
[in]An object of a trade request. Onlydealer actions(200-255) can be set as a request type inIMTRequest::Action.

**sink**  
[in] A pointer to the object that implements theIMTDealerSinkinterface, to which the result of trade request execution is passed asynchronously. To unsubscribe from receipt of the result, theIMTManagerAPI::DealerUnsubscribemethod is used. If you don't need any notification, pass nullptr as a value.

**id**  
[out] The ID assigned to the sent request (IMTRequest::IDClient). This ID allows the application to identify its own requests in the stream when receiving the answers from the trade server in theIMTDealerSinkinterface. The ID is only unique within the current connection of the application. Requests from several clients/API can have the same IDs. Therefore, it makes sense to analyze the identifier only from the application which fills it.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred which corresponds to the response code. The MT_RET_OK response code only means that the request has successfully been sent to the trade server. The execution result should be tracked in the [IMTDealerSink::OnDealerResult](../../../Dealer-Interface/OnDealerResult.md) or [IMTDealerSink::OnDealerAnswer](../../../Dealer-Interface/OnDealerAnswer.md) handlers.

### Note

An answer to a trade request is formed in two forms - [IMTDealerSink::OnDealerResult](../../../Dealer-Interface/OnDealerResult.md) and [IMTDealerSink::OnDealerAnswer](../../../Dealer-Interface/OnDealerAnswer.md).
