[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerGetAsync

[Previous](DealerStop.md) | [Next](DealerLockAsync.md)

# IMTGatewayAPI::DealerGetAsync

Capture the most early (old) request from the requests queue.

C++
    
    
    MTAPIRES  IMTGatewayAPI::DealerGetAsync()

.NET
    
    
    MTRetCode  CIMTGatewayAPI.DealerGetAsync()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Request object captured as a result of this method calling is returned in the [IMTGatewaySink::OnDealerLock](../../Event-Interface/OnDealerLock.md) method.
