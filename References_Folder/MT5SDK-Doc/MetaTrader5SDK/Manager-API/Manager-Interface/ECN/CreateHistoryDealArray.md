[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [ECN](../ECN.md) / CreateHistoryDealArray

[Previous](CreateHistoryDeal.md) | [Next](RequestByGroup.md)

# IMTManagerAPI::ECNCreateHistoryDealArray

Create an object of an array of deals from the ECN history.

C++
    
    
    IMTECNHistoryDealArray*  IMTManagerAPI::ECNCreateHistoryDealArray()

.NET
    
    
    IMTECNHistoryDealArray  CIMTManagerAPI.ECNCreateHistoryDealArray()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryFilling](../../../Database-Interfaces/ECN/IMTHistoryDealArray.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryDealArray::Release](../../../Database-Interfaces/ECN/IMTECNHistoryDealArray/IMTHistoryDealArray-Release.md) method of this object.
