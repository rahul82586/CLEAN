[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineCreate

[Previous](../Online-Connections.md) | [Next](OnlineCreateArray.md)

# IMTManagerAPI::OnlineCreate

Create connection record object.

C++
    
    
    IMTOnline*  IMTManagerAPI::OnlineCreate()

.NET
    
    
    CIMTOnline  CIMTManagerAPI::OnlineCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTOnline](../../../Database-Interfaces/Online-Connections/IMTOnline.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling [IMTOnline::Release](../../../Database-Interfaces/Online-Connections/IMTOnline/Release.md) method of this object.
