[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / PositionNext

[Previous](PositionTotal.md) | [Next](PositionGet.md)

# IMTDaily::PositionNext

Get a [trade position](../../Positions.md) by the index.

C++
    
    
    MTAPIRES  IMTDaily::PositionNext(
       const UINT    pos,          // Position in the list
       IMTPosition*  position      // Position object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.PositionNext(
       uint          pos,          // Position in the list
       CIMTPosition  position      // Position object
       )

### Parameters

**pos**  
[in] Position of a trade position, starting with 0.

**position**  
[out] An object of a trade position. The 'position' object must be first created using theIMTManagerAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method copies parameters of a trade position with a specified index to the position object.
