[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Summary Positions](../Summary-Positions.md) / SummaryCreate

[Previous](../Summary-Positions.md) | [Next](SummaryCreateArray.md)

# IMTManagerAPI::SummaryCreate

Create an object of the summary of clients' positions.

C++
    
    
    IMTSummary*  IMTManagerAPI::SummaryCreate()

.NET
    
    
    CIMTSummary  CIMTManagerAPI.SummaryCreate()

### Return Value

It returns a pointer to the created object that implements the [IMTSummary](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummary.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTSummary::Release](../../../Database-Interfaces/Trade/Summary-Positions/IMTSummary/Release.md) method of this object.
