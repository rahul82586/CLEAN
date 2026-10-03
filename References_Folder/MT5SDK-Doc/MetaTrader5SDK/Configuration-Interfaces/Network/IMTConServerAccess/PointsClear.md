[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PointsClear

[Previous](PointsDelete.md) | [Next](PointsTotal.md)

# IMTConServerAccess::PointsClear

Clear the list of access points.

C++
    
    
    MTAPIRES  IMTConServerAccess::PointsClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.PointsClear()

Python (Manager API)
    
    
    MTConServerAccess.PointsClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method clears the list of server access points.
