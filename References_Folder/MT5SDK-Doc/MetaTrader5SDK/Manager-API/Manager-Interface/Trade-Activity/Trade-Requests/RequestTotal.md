[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Trade Requests](../Trade-Requests.md) / RequestTotal

[Previous](RequestUnsubscribe.md) | [Next](RequestNext.md)

# IMTManagerAPI::RequestTotal

Get the total amount of trade requests in a requests queue.

C++
    
    
    UINT  IMTManagerAPI::RequestTotal()

.NET
    
    
    uint  CIMTManagerAPI.RequestTotal()

Python
    
    
    ManagerAPI.RequestTotal()

### Return Value

Total amount of trade requests in a requests queue.

### Note

To use this method, you must first call [IMTManagerAPI::DealerStart](../Dealing/DealerStart.md).
