[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionCreate

[Previous](../Positions.md) | [Next](PositionCreateArray.md)

# IMTReportAPI::PositionCreate

Create an object of a trade position.
    
    
    IMTPosition*  IMTReportAPI::PositionCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTPosition](../../../../Database-Interfaces/Trade/Positions/IMTPosition.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTPosition::Release](../../../../Database-Interfaces/Trade/Positions/IMTPosition/Release.md) method of this object.
