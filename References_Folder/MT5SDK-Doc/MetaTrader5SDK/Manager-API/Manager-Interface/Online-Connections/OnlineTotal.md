[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineTotal

[Previous](OnlineCreateArray.md) | [Next](OnlineNext.md)

# IMTManagerAPI::OnlineTotal

Get the total amount of the current connections to the trade server.

C++
    
    
    UINT  IMTManagerAPI::OnlineTotal()

.NET
    
    
    uint  CIMTManagerAPI.OnlineTotal()

Python
    
    
    ManagerAPI.OnlineTotal()

### Return Value

Amount of the current connections to the trade server.

### Notes

All types of connection are considered, including client, manager and API ones with the exception of the cluster components' (platform servers') connections.
