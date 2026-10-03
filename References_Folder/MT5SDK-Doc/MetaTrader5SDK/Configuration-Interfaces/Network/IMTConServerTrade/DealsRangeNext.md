[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DealsRangeNext

[Previous](DealsRangeTotal.md) | [Next](TotalUsers.md)

# IMTConServerTrade::DealsRangeNext

Get a range of [deals](../../../Database-Interfaces/Trade/Deals.md) by the index.

C++
    
    
    MTAPIRES  IMTConServerTrade::DealsRangeNext(
       const UINT          pos,       // Position of the range
       IMTConServerRange*  range      // Range object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.DealsRangeNext(
       uint                pos,       // Position of the range
       CIMTConServerRange  range      // Range object
       )

Python (Manager API)
    
    
    MTConServerTrade.DealsRangeNext(
       pos,                # Position of the range
       range               # Range object
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**range**  
[out] An object of the range. The 'range' object must first be created using theIMTAdminAPI::NetServerRangeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the range of deals with a specified index to the range object.
