[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateHistoryMatchingArray

[Previous](CreateHistoryMatching.md) | [Next](CreateHistoryFilling.md)

# IMTAdminAPI::ECNCreateHistoryMatchingArray

Create an array of matching order objects from history.

C++
    
    
    IMTECNHistoryMatchingArray*  IMTAdminAPI::ECNCreateHistoryMatchingArray()

.NET
    
    
    CIMTECNHistoryMatchingArray  CIMTAdminAPI.ECNCreateHistoryMatchingArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryMatchingArray](../../../Database-Interfaces/ECN/IMTHistoryMatchingArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryMatchingArray::Release](../../../Database-Interfaces/ECN/IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Release.md) method of this object.
