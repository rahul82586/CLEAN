[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestGetAll

[Previous](RequestGet.md) | [Next](../Gateway-Symbols.md)

# IMTGatewayAPI::RequestGetAll

Get all the trade requests in a queue.

C++
    
    
    MTAPIRES  IMTGatewayAPI::RequestGetAll(
       IMTRequestArray*  requests      // An object of the array of requests
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.RequestGetAll(
       CIMTRequestArray  requests      // An object of the array of requests
       )

### Parameters

**requests**  
[out] An object of the array of requests. The requests object must first be created using theIMTGatewaAPI::RequestArrayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies the array of trade requests in a queue to the requests object. [IMTGatewayAPI::DealerStart](../Processing-Trade-Requests/DealerStart.md) must be preliminarily called for making the method work.
