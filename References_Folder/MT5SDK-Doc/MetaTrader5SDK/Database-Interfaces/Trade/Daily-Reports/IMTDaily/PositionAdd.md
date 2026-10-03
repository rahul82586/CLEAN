[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / PositionAdd

[Previous](DailyInterest.md) | [Next](PositionUpdate.md)

# IMTDaily::PositionAdd

Add a [trade position](../../Positions.md) to the daily report.

C++
    
    
    MTAPIRES  IMTDaily::PositionAdd(
       IMTPosition*  position      // An object of a trade position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.PositionAdd(
       CIMTPosition  position      // An object of a trade position
       )

### Parameters

**position**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
