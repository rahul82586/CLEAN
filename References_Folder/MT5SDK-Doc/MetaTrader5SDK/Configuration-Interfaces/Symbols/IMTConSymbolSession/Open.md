[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / Open

[Previous](Clear.md) | [Next](OpenHours.md)

# IMTConSymbolSession::Open

Get the opening time of trading or quoting session of a symbol.

C++
    
    
    UINT  IMTConSymbolSession::Open()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbolSession.Open()

Python (Manager API)
    
    
    MTConSymbolSession.Open

### Return Value

The session opening time in minutes from 00:00. For example, 100 denotes 01:40.

# IMTConSymbolSession::Open

Set the opening time of trading or quoting session of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbolSession::Open(
       const UINT  open      // Session opening time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolSession.Open(
       uint        open      // Session opening time
       )

Python (Manager API)
    
    
    MTConSymbolSession.Open

### Parameters

**open**  
[in] The opening time of a trading or quoting session in minutes elapsed since 00:00. For example, 100 denotes 01:40.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
