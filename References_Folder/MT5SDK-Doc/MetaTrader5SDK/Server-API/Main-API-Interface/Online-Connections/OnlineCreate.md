[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineCreate

[Previous](../Online-Connections.md) | [Next](OnlineCreateArray.md)

# IMTServerAPI::OnlineCreate

Create connection record object.
    
    
    IMTUser*  IMTServerAPI::OnlineCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTOnline](../../../Database-Interfaces/Online-Connections/IMTOnline.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOnline::Release](../../../Database-Interfaces/Online-Connections/IMTOnline/Release.md) method of this object.
