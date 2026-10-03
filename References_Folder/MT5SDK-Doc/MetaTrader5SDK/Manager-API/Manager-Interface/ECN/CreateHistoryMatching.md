[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / CreateHistoryMatching

[Previous](CreateProviderArray.md) | [Next](CreateHistoryMatchingArray.md)

# IMTManagerAPI::ECNCreateHistoryMatching

Create an object of a matching order from history.

C++
    
    
    IMTECNHistoryMatching*  IMTManagerAPI::ECNCreateHistoryMatching()

.NET
    
    
    CIMTECNHistoryMatching  CIMTManagerAPI.ECNCreateHistoryMatching()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryFillingArray](../../../Database-Interfaces/ECN/IMTHistoryMatching.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryMatching::Release](../../../Database-Interfaces/ECN/IMTECNHistoryMatching/IMTHistoryMatching-Release.md) method of this object.
