[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon NameFull

[Previous](IMTCon-Name.md) | [Next](IMTCon-Owner.md)

# IMTConCommon::NameFull

Get the full name of the platform.

C++
    
    
    LPCWSTR  IMTConCommon::NameFull()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.NameFull()

Python (Manager API)
    
    
    MTConCommon.NameFull

### Return Value

If successful, it returns a pointer to a string with the full name of the . Otherwise, it returns NULL.

### Note

The full name of the platform is formed of [IMTConCommon::OwnerID](IMTCon-OwnerID.md) \- [IMTConCommon::Name](IMTCon-Name.md).
