[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / PositionClear

[Previous](PositionDelete.md) | [Next](PositionShift.md)

# IMTDaily::PositionClear

Clear the list of [positions](../../Positions.md) in a daily report.

C++
    
    
    MTAPIRES  IMTDaily::PositionClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.PositionClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears the entire list of positions in a daily report.
