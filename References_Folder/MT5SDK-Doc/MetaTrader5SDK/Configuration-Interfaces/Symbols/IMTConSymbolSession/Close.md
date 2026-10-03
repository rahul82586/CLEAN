[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolSession](../IMTConSymbolSession.md) / Close

[Previous](OpenMinutes.md) | [Next](CloseHours.md)

# IMTConSymbolSession::Close

Get the closing time of trading or quoting session of a symbol.

C++
    
    
    UINT  IMTConSymbolSession::Close()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConSymbolSession.Close()

Python (Manager API)
    
    
    MTConSymbolSession.Close

### Return Value

The session closing time in minutes from 00:00. For example, 100 denotes 01:40.

# IMTConSymbolSession::Close

Set the closing time of trading or quoting session of a symbol.

C++
    
    
    MTAPIRES  IMTConSymbolSession::Close(
       const UINT  close      // Session closing time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbolSession.Close(
       uint        close      // Session closing time
       )

Python (Manager API)
    
    
    MTConSymbolSession.Close

### Parameters

**close**  
[in] The closing time of a trading or quoting session in minutes elapsed since 00:00. For example, 100 denotes 01:40.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
