[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [ECN](../ECN.md) / CreateHistoryDeal

[Previous](CreateHistoryFillingArray.md) | [Next](CreateHistoryDealArray.md)

# IMTAdminAPI::ECNCreateHistoryDeal

Create an object of a deal from the ECN history.

C++
    
    
    IMTECNHistoryDeal*  IMTAdminAPI::ECNCreateHistoryDeal()

.NET
    
    
    CIMTECNHistoryDeal  CIMTAdminAPI.ECNCreateHistoryDeal()

### Return Value

The function returns a pointer to the created object that implements the [IMTECNHistoryFilling](../../../Database-Interfaces/ECN/IMTHistoryDeal.md) interface. Null is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTECNHistoryDeal::Release](../../../Database-Interfaces/ECN/IMTECNHistoryDeal/IMTHistoryDeal-Release.md) method of this object.
