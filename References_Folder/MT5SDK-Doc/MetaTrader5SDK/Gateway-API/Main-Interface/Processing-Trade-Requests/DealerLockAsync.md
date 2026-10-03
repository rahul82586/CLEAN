[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Processing Trade Requests](../Processing-Trade-Requests.md) / DealerLockAsync

[Previous](DealerGetAsync.md) | [Next](DealerAnswerAsync.md)

# IMTGatewayAPI::DealerLockAsync

Capture a request from the requests queue by ID.

C++
    
    
    MTAPIRES  IMTGatewayAPI::DealerLockAsync(
       const UINT  id      // Request ID
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.DealerLockAsync(
       uint  id           // Request ID
       )

### Parameters

**id**  
[in] ID of the request that is to be captured. TheIMTRequest::IDvalue is used as the identifier..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code. Code MT_RET_OK_NONE means that the request is no longer available on the trade server. For example, it could have been captured by another dealer or application.

### Note

Request object captured as a result of this method calling is returned in the [IMTGatewaySink::OnDealerLock](../../Event-Interface/OnDealerLock.md) method.
