[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineTotal

[Previous](OnlineCreateArray.md) | [Next](OnlineNext.md)

# IMTServerAPI::OnlineTotal

Get the total amount of the current connections to the trade server.
    
    
    UINT  IMTServerAPI::OnlineTotal()

### Return Value

Amount of the current connections to the trade server.

### Notes

All types of connection are considered, including client, manager and API ones with the exception of the cluster components' (platform servers') connections.
