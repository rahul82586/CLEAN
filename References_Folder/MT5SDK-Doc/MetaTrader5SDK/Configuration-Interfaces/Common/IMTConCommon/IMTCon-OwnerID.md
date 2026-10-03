[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon OwnerID

[Previous](IMTCon-Owner.md) | [Next](IMTCon-OwnerHost.md)

# IMTConCommon::OwnerID

Get a short name of the owner of the platform.

C++
    
    
    LPCWSTR  IMTConCommon::OwnerID()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.OwnerID()

Python (Manager API)
    
    
    MTConCommon.OwnerID

### Return Value

If successful, it returns a pointer to a string with the short name of the owner of the platform. Otherwise, it returns NULL.

### Note

Owner's short name is specified in the platform license.
