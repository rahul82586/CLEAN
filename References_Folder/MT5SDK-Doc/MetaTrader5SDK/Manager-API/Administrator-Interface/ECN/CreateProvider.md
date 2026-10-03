[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateProvider

[Previous](CreateFillingArray.md) | [Next](CreateProviderArray.md)

# IMTAdminAPI::ECNCreateProvider

Create an object of a provider via which orders are executed.

C++
    
    
    IMTECNProvider*  IMTAdminAPI::ECNCreateProvider()

.NET
    
    
    CIMTECNProvider  CIMTAdminAPI.ECNCreateProvider()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNProvider](../../../Database-Interfaces/ECN/IMTProvider.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNProvider::Release](../../../Database-Interfaces/ECN/IMTECNProvider/IMTProvider-Release.md) method of this object.
