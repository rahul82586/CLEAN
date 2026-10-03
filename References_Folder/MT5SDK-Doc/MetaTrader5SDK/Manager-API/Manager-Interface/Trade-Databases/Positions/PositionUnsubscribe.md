[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionUnsubscribe

[Previous](PositionSubscribe.md) | [Next](PositionGet.md)

# IMTManagerAPI::PositionUnsubscribe

Unsubscribe from the events associated with changes in the database of positions.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionUnsubscribe(
       IMTPositionSink*  sink      // A pointer to the IMTPositionSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionUnsubscribe(
       CIMTPositionSink  sink      // CIMTPositionSink object
       )

Python
    
    
    ManagerAPI.PositionUnsubscribe(
       sink              # IMTPositionSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTPositionSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::PositionSubscribe](PositionSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
