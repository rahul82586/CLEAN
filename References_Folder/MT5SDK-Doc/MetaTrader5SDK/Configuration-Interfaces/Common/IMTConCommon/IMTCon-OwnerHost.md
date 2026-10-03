[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon OwnerHost

[Previous](IMTCon-OwnerID.md) | [Next](IMTCon-OwnerEmail.md)

# IMTConCommon::OwnerHost

Get the host address of the platform owner.

C++
    
    
    LPCWSTR  IMTConCommon::OwnerHost()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.OwnerHost()

Python (Manager API)
    
    
    MTConCommon.OwnerHost

### Return Value

If successful, it returns a pointer to a string with the host address of the owner of the platform. Otherwise, it returns NULL.

### Note

The platform owner's host address is specified in the license.

A pointer to the resulting string is valid for the lifetime of the [IMTConCommon](../IMTCon.md) object.

To use the string after the object removal (call of the [IMTConCommon::Release](IMTCon-Release.md) method of this object), a copy of it should be created.

The maximum length of the address is 128 characters (including the sign of the string end).
