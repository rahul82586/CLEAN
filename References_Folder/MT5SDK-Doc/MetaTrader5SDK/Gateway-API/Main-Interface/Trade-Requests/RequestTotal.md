[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestTotal

[Previous](RequestUnsubscribe.md) | [Next](RequestNext.md)

# IMTGatewayAPI::RequestTotal

Get the total amount of trade requests in a requests queue.

C++
    
    
    UINT  IMTGatewayAPI::RequestTotal()

.NET
    
    
    uint  CIMTGatewayAPI.RequestTotal()

### Return Value

Total amount of trade requests in a requests queue.

### Note

[IMTGatewayAPI::DealerStart](../Processing-Trade-Requests/DealerStart.md) must be preliminarily called for making this method work.
