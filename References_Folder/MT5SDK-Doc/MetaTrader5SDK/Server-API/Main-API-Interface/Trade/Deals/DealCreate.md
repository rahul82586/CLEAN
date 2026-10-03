[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealCreate

[Previous](../Deals.md) | [Next](DealCreateArray.md)

# IMTServerAPI::DealCreate

Create an object of a deal.
    
    
    IMTDeal*  IMTServerAPI::DealCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDeal](../../../../Database-Interfaces/Trade/Deals/IMTDeal.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTDeal::Release](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Release.md) method of this object.
