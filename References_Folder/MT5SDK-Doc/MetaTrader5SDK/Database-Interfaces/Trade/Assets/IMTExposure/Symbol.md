[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposure](../IMTExposure.md) / Symbol

[Previous](Clear.md) | [Next](Digits.md)

# IMTExposure::Symbol

Gets the name of an asset.

C++
    
    
    LPCWSTR  IMTExposure::Symbol()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTExposure.Symbol()

### Return Value

If successful, it returns a pointer to a string with the name of the asset. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTExposure](../IMTExposure.md) method.
