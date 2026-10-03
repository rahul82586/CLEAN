[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickSubscribe

[Previous](../Tick-Data.md) | [Next](TickUnsubscribe.md)

# IMTManagerAPI::TickSubscribe

Subscribe to the events associated with changes in the database of price data.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickSubscribe(
       IMTTickSink*  sink      // A pointer to the IMTTickSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickSubscribe(
       CIMTTickSink  sink      // CIMTTickSink object
       )

Python
    
    
    ManagerAPI.TickSubscribe(
       sink          # IMTTickSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTTickSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The Manager API application only receives ticks for the [selected symbols](../Selected-Symbols.md).
