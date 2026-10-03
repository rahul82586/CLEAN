[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateMatching

[Previous](../ECN.md) | [Next](CreateMatchingArray.md)

# IMTAdminAPI::ECNCreateMatching

Create a matching order object.

C++
    
    
    IMTECNMatching*  IMTAdminAPI::ECNCreateMatching()

.NET
    
    
    CIMTECNMatching  CIMTAdminAPI.ECNCreateMatching()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNMatching](../../../Database-Interfaces/ECN/IMTMatching.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNMatching::Release](../../../Database-Interfaces/ECN/IMTECNMatching/IMTMatching-Release.md) method of this object.
