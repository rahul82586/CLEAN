[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Trade Requests](../Trade-Requests.md) / RequestCreate

[Previous](../Trade-Requests.md) | [Next](RequestCreateArray.md)

# IMTManagerAPI::RequestCreate

Create an object of a trade request.

C++
    
    
    IMTRequest*  IMTManagerAPI::RequestCreate()

.NET
    
    
    CIMTRequest  CIMTManagerAPI.RequestCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTRequest](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequest.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTRequest::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequest/Requests-Release.md) method of this object.
