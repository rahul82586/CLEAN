[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateFillingArray

[Previous](CreateFilling.md) | [Next](CreateProvider.md)

# IMTAdminAPI::ECNCreateFillingArray

Create an array of filling objects.

C++
    
    
    IMTECNFillingArray*  IMTAdminAPI::ECNCreateFillingArray()

.NET
    
    
    CIMTECNFillingArray  CIMTAdminAPI.ECNCreateFillingArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNFillingArray](../../../Database-Interfaces/ECN/IMTFillingArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNFillingArray::Release](../../../Database-Interfaces/ECN/IMTECNFillingArray/IMTFillingArray-Release.md) method of this object.
