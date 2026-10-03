[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineCreateArray

[Previous](OnlineCreate.md) | [Next](OnlineTotal.md)

# IMTServerAPI::OnlineCreateArray

Create connection record array object.
    
    
    IMTOrderArray*  IMTServerAPI::OnlineCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTOnlineArray](../../../Database-Interfaces/Online-Connections/IMTOnlineArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOnlineArray::Release](../../../Database-Interfaces/Online-Connections/IMTOnlineArray/Release.md) method of this object.
