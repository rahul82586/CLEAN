[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionSubscribe

[Previous](PositionCreateArray.md) | [Next](PositionUnsubscribe.md)

# IMTManagerAPI::PositionSubscribe

Subscribe to the events associated with changes in the database of positions.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionSubscribe(
       IMTPositionSink*  sink      // A pointer to the IMTPositionSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionSubscribe(
       CIMTPositionSink  sink      // CIMTPositionSink object
       )

Python
    
    
    ManagerAPI.PositionSubscribe(
       sink              # IMTPositionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTPositionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTPositionSink](../../../../Database-Interfaces/Trade/Positions/IMTPositionSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../../Return-Codes/Common-errors.md) is returned.
