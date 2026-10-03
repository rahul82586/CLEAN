[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon OwnerEmail

[Previous](IMTCon-OwnerHost.md) | [Next](IMTCon-Product.md)

# IMTConCommon::OwnerEmail

Get email address of the owner of the platform.

C++
    
    
    LPCWSTR  IMTConCommon::OwnerEmail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.OwnerEmail()

Python (Manager API)
    
    
    MTConCommon.OwnerEmail

### Return Value

If successful, it returns a pointer to a string with the email address of the platform owner. Otherwise, it returns NULL.

### Note

The platform owner's email is specified in the license.
