[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestCreate

[Previous](../Trade-Requests.md) | [Next](RequestArrayCreate.md)

# IMTGatewayAPI::RequestCreate

Create an object of a trade request.

C++
    
    
    IMTRequest*  IMTGatewayAPI::RequestCreate()

.NET
    
    
    CIMTRequest  CIMTGatewayAPI.RequestCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTRequest](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTRequest::Release](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Release.md) method of this object.
