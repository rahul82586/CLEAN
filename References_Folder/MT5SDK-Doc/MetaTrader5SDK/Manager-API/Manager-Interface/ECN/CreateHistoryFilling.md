[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / CreateHistoryFilling

[Previous](CreateHistoryMatchingArray.md) | [Next](CreateHistoryFillingArray.md)

# IMTManagerAPI::ECNCreateHistoryFilling

Create an object of a filling order from history.

C++
    
    
    IMTECNHistoryFilling*  IMTManagerAPI::ECNCreateHistoryFilling()

.NET
    
    
    CIMTECNHistoryFilling  CIMTManagerAPI.ECNCreateHistoryFilling()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryFilling](../../../Database-Interfaces/ECN/IMTHistoryFilling.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryFilling::Release](../../../Database-Interfaces/ECN/IMTECNHistoryFilling/IMTHistoryFilling-Release.md) method of this object.
