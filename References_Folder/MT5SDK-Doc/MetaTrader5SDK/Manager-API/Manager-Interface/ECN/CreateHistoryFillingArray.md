[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / CreateHistoryFillingArray

[Previous](CreateHistoryFilling.md) | [Next](CreateHistoryDeal.md)

# IMTManagerAPI::ECNCreateHistoryFillingArray

Create an array of filling order objects from history.

C++
    
    
    IMTECNHistoryFillingArray*  IMTManagerAPI::ECNCreateHistoryFillingArray()

.NET
    
    
    CIMTECNHistoryFillingArray  CIMTManagerAPI.ECNCreateHistoryFillingArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryFillingArray](../../../Database-Interfaces/ECN/IMTHistoryFillingArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryFillingArray::Release](../../../Database-Interfaces/ECN/IMTECNHistoryFillingArray/IMTHistoryFillingArray-Release.md) method of this object.
