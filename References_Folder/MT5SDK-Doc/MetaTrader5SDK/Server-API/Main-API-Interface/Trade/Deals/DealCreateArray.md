[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Deals](../Deals.md) / DealCreateArray

[Previous](DealCreate.md) | [Next](DealSubscribe.md)

# IMTServerAPI::DealCreateArray

Create an object of the array of deals.
    
    
    IMTDealArray*  IMTServerAPI::DealCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTDealArray](../../../../Database-Interfaces/Trade/Deals/IMTDealArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTDealArray::Release](../../../../Database-Interfaces/Trade/Deals/IMTDealArray/Release.md) method of this object.
