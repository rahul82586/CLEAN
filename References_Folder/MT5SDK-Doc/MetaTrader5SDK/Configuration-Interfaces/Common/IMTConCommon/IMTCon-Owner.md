[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon Owner

[Previous](IMTCon-NameFull.md) | [Next](IMTCon-OwnerID.md)

# IMTConCommon::Owner

Get the full name of the owner of the platform.

C++
    
    
    LPCWSTR  IMTConCommon::Owner()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.Owner()

Python (Manager API)
    
    
    MTConCommon.Owner

### Return Value

If successful, it returns a pointer to a string with the full name of the owner of the platform. Otherwise, it returns NULL.

### Note

Owner's full name is specified in the platform license.
