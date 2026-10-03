[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / PositionUpdate

[Previous](PositionAdd.md) | [Next](PositionDelete.md)

# IMTDaily::PositionUpdate

Modify a [trade position](../../Positions.md) in a daily report by its index.

C++
    
    
    MTAPIRES  IMTDaily::PositionUpdate(
       const UINT          pos,          // Position in the list
       const IMTPosition*  position      // An object of a trade position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.PositionUpdate(
       uint                pos,          // Position in the list
       CIMTPosition        position      // An object of a trade position
       )

### Parameters

**pos**  
[in] The position of a trade position in the list, starting with 0.

**position**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
