[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / PositionGet

[Previous](PositionNext.md) | [Next](OrderAdd.md)

# IMTDaily::PositionGet

Get a [trade position](../../Positions.md) by symbol name.

C++
    
    
    MTAPIRES  IMTDaily::PositionGet(
       LPCWSTR       symbol,       // Symbol name
       IMTPosition*  position      // Position object
       )  const

.NET (Gateway/Manager API)
    
    
    MTAPIRES  IMTDaily::PositionGet(
       string        symbol,       // Symbol name
       CIMTPosition  position      // Position object
       )

### Parameters

**symbol**  
[in] Symbol name.

**position**  
[out] An object of a trade position. The 'position' object must be first created using theIMTManagerAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The [IMTConSymbol::Symbol](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/Symbol.md) value is used as the symbol name.
