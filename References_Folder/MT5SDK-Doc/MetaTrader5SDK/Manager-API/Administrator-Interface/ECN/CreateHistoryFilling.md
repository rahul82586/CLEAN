[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateHistoryFilling

[Previous](CreateHistoryMatchingArray.md) | [Next](CreateHistoryFillingArray.md)

# IMTAdminAPI::ECNCreateHistoryFilling

Create an object of a filling order from history.

C++
    
    
    IMTECNHistoryFilling*  IMTAdminAPI::ECNCreateHistoryFilling()

.NET
    
    
    CIMTECNHistoryFilling  CIMTAdminAPI.ECNCreateHistoryFilling()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryFilling](../../../Database-Interfaces/ECN/IMTHistoryFilling.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryFilling::Release](../../../Database-Interfaces/ECN/IMTECNHistoryFilling/IMTHistoryFilling-Release.md) method of this object.
