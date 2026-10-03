[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / AccessNext

[Previous](AccessTotal.md) | [Next](ReportAdd.md)

# IMTConManager::AccessNext

Get a range of IP addresses, from which a manager is allowed to connect to the platform, based on its position in the list.

C++
    
    
    MTAPIRES  IMTConManager::AccessNext(
       const UINT            pos,        // Position of the range
       IMTConManagerAccess*  access      // An object of the range of addresses
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.AccessNext(
       uint                  pos,        // Position of the range
       CIMTConManagerAccess  access      // An object of the range of addresses
       )

Python (Manager API)
    
    
    MTConManager.AccessNext(
       pos                   # Position of the range
       )
    
    
    MTConManager.AccessGet()

### Parameters

**pos**  
[in] Position of a range of addresses in the list, starting with 0.

**access**  
[out] An object of the range of addresses. The access object must be first created using theIMTAdminAPI::ManagerAccessCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
