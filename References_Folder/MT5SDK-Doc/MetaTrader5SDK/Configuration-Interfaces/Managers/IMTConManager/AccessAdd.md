[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / AccessAdd

[Previous](GroupNext.md) | [Next](AccessUpdate.md)

# IMTConManager::AccessAdd

Create a range of IP addresses, from which a manager is allowed to connect to the platform.

C++
    
    
    MTAPIRES  IMTConManager::AccessAdd(
       IMTConManagerAccess*  access      // An object of the range of addresses
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.AccessAdd(
       CIMTConManagerAccess  access      // An object of the range of addresses
       )

Python (Manager API)
    
    
    MTConManager.AccessAdd(
       access                # An object of the range of addresses
       )

### Parameters

**access**  
[in] An object of the range of addresses.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
