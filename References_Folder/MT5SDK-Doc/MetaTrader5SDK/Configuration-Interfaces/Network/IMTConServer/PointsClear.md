[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / PointsClear

[Previous](PointsDelete.md) | [Next](PointsTotal.md)

# IMTConServer::PointsClear

Clear the list of access points.

C++
    
    
    MTAPIRES  IMTConServer::PointsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.PointsClear()

Python (Manager API)
    
    
    MTConServer.PointsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of server access points.
