[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Trade Requests](../Trade-Requests.md) / RequestCreateArray

[Previous](RequestCreate.md) | [Next](RequestSubscribe.md)

# IMTManagerAPI::RequestCreateArray

Create an object of the array of trade requests.

C++
    
    
    IMTRequestArray*  IMTManagerAPI::RequestCreateArray()

.NET
    
    
    CIMTRequestArray  CIMTManagerAPI.RequestCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTRequestArray](../../../../Database-Interfaces/Trade/Trade-Requests/Requests-IMTRequestArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTRequestArray::Release](../../../../Database-Interfaces/Trade/Trade-Requests/IMTRequestArray/Requests-Release.md) method of this object.
