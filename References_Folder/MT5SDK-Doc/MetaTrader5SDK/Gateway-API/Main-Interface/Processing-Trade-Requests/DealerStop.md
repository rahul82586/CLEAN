[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerStop

[Previous](DealerStart.md) | [Next](DealerGetAsync.md)

# IMTGatewayAPI::DealerStop

[DealerStart](DealerStart.md) inverse method. After its successful execution the gateway will stop fulfilling the dealer functions.

C++
    
    
    MTAPIRES  IMTGatewayAPI::DealerStop()

.NET
    
    
    MTRetCode  CIMTGatewayAPI.DealerStop()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
