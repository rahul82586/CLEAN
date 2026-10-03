[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / CreateHistoryMatchingArray

[Previous](CreateHistoryMatching.md) | [Next](CreateHistoryFilling.md)

# IMTManagerAPI::ECNCreateHistoryMatchingArray

Create an array of matching order objects from history.

C++
    
    
    IMTECNHistoryMatchingArray*  IMTManagerAPI::ECNCreateHistoryMatchingArray()

.NET
    
    
    CIMTECNHistoryMatchingArray  CIMTManagerAPI.ECNCreateHistoryMatchingArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryMatchingArray](../../../Database-Interfaces/ECN/IMTHistoryMatchingArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryMatchingArray::Release](../../../Database-Interfaces/ECN/IMTECNHistoryMatchingArray/IMTHistoryMatchingArray-Release.md) method of this object.
