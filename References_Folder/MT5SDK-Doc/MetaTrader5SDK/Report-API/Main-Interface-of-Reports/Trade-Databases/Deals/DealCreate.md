[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealCreate

[Previous](../Deals.md) | [Next](DealCreateArray.md)

# IMTReportAPI::DealCreate

Create an object of a deal.
    
    
    IMTDeal*  IMTReportAPI::DealCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTDeal](../../../../Database-Interfaces/Trade/Deals/IMTDeal.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTDeal::Release](../../../../Database-Interfaces/Trade/Deals/IMTDeal/Release.md) method of this object.
