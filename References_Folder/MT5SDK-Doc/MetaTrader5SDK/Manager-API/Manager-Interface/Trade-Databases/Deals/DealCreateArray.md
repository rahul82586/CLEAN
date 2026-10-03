[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealCreateArray

[Previous](DealCreate.md) | [Next](DealSubscribe.md)

# IMTManagerAPI::DealCreateArray

Create an object of the array of deals.

C++
    
    
    IMTDealArray*  IMTManagerAPI::DealCreateArray()

.NET
    
    
    CIMTDealArray  CIMTManagerAPI.DealCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTDealArray](../../../../Database-Interfaces/Trade/Deals/IMTDealArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTDealArray::Release](../../../../Database-Interfaces/Trade/Deals/IMTDealArray/Release.md) method of this object.
