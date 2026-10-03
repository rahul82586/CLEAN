[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummaryCreateArray

[Previous](SummaryCreate.md) | [Next](SummarySubscribe.md)

# IMTManagerAPI::SummaryCreateArray

Create an array of objects of the summary of clients' positions.

C++
    
    
    IMTSummaryArray*  IMTManagerAPI::SummaryCreateArray()

.NET
    
    
    CIMTSummaryArray  CIMTManagerAPI.SummaryCreateArray()

### Return Value

It returns a pointer to the created object that implements the [IMTSummaryArray](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummaryArray.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTSummary::Release](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummaryArray/Release.md) method of this object.
