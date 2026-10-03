[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateFilling

[Previous](CreateMatchingArray.md) | [Next](CreateFillingArray.md)

# IMTAdminAPI::ECNCreateFilling

Create a filling order object.

C++
    
    
    IMTECNFilling*  IMTAdminAPI::ECNCreateFilling()

.NET
    
    
    CIMTECNFilling  CIMTAdminAPI.ECNCreateFilling()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNFilling](../../../Database-Interfaces/ECN/IMTFilling.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNFilling::Release](../../../Database-Interfaces/ECN/IMTECNFilling/IMTFilling-Release.md) method of this object.
