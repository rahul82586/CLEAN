[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Tick Data](../Tick-Data.md) / TickUnsubscribe

[Previous](TickSubscribe.md) | [Next](TickAdd.md)

# IMTManagerAPI::TickUnsubscribe

Unsubscribe from the events associated with changes in the database of price data.

C++
    
    
    MTAPIRES  IMTManagerAPI::TickUnsubscribe(
       IMTTickSink*  sink      // A pointer to the IMTTickSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TickUnsubscribe(
       CIMTTickSink  sink      // CIMTTickSink object
       )

Python
    
    
    ManagerAPI.TickUnsubscribe(
       sink          # IMTTickSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTTickSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::TickSubscribe](TickSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
