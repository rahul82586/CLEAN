[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionCreateArray

[Previous](PositionCreate.md) | [Next](PositionGet.md)

# IMTReportAPI::PositionCreateArray

Create an object of the array of trade positions.
    
    
    IMTPositionArray*  IMTReportAPI::PositionCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTPositionArray](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTPositionArray::Release](../../../../Database-Interfaces/Trade/Positions/IMTPositionArray/Release.md) method of this object.
