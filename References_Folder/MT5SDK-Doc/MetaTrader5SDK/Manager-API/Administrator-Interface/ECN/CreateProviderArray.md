[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateProviderArray

[Previous](CreateProvider.md) | [Next](CreateHistoryMatching.md)

# IMTAdminAPI::ECNCreateProviderArray

Create an object of the array of providers via which orders are executed.

C++
    
    
    IMTECNProviderArray*  IMTAdminAPI::ECNCreateProviderArray()

.NET
    
    
    CIMTECNProviderArray  CIMTAdminAPI.ECNCreateProviderArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNProviderArray](../../../Database-Interfaces/ECN/IMTProviderArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNProviderArray::Release](../../../Database-Interfaces/ECN/IMTECNProviderArray/IMTProviderArray-Release.md) method of this object.
