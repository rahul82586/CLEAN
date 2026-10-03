[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon Product

[Previous](IMTCon-OwnerEmail.md) | [Next](IMTCon-ExpirationLicense.md)

# IMTConCommon::Product

Get the full name of the product.

C++
    
    
    LPCWSTR  IMTConCommon::Product()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.Product()

Python (Manager API)
    
    
    MTConCommon.Product

### Return Value

If successful, it returns a pointer to a string with the full name of the product. Otherwise, it returns NULL.

### Note

The full product name is specified in the license.
