[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Trade Requests](../Trade-Requests.md) / RequestArrayCreate

[Previous](RequestCreate.md) | [Next](RequestSubscribe.md)

# IMTGatewayAPI::RequestArrayCreate

Create an object of the array of trade requests.

C++
    
    
    IMTRequestArray*  IMTGatewayAPI::RequestArrayCreate()

.NET
    
    
    CIMTRequestArray  CIMTGatewayAPI.RequestArrayCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTRequestArray](../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTRequestArray::Release](../../../Database-Interfaces/Trade/Trade-Requests/IMTRequestArray/Requests-Release.md) method of this object.
