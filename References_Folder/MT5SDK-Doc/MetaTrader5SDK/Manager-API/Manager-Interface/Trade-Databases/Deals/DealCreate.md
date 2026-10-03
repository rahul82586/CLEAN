[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealCreate

[Previous](../Deals.md) | [Next](DealCreateArray.md)

# IMTManagerAPI::DealCreate

Create an object of a deal.

C++
    
    
    IMTDeal*  IMTManagerAPI::DealCreate()

.NET
    
    
    CIMTDeal  CIMTManagerAPI.DealCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDeal](../../../../Database-Interfaces/Trade/Deals/IMTDeal.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTDeal::Release](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Release.md) method of this object.
