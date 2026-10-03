[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealCreateArray

[Previous](DealCreate.md) | [Next](DealRequest.md)

# IMTAdminAPI::DealCreateArray

Create an object of the array of deals.

C++
    
    
    IMTDealArray*  IMTAdminAPI::DealCreateArray()

.NET
    
    
    CIMTDealArray  CIMTAdminAPI.DealCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTDealArray](../../../../Database-Interfaces/Trade/Deals/IMTDealArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTDealArray::Release](../../../../Database-Interfaces/Trade/Deals/IMTDealArray/Release.md) method of this object.
