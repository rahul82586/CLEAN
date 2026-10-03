[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadUnsubscribe

[Previous](SpreadSubscribe.md) | [Next](SpreadAdd.md)

# IMTGatewayAPI::SpreadUnsubscribe

Unsubscribe from events and hooks associated with spread configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SpreadUnsubscribe(
       IMTConSpreadSink*  sink      // pointer to IMTConSpreadSink object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SpreadUnsubscribe(
       CIMTConSpreadSink  sink      // CIMTConSpreadSink object
       )

### Parameters

**sink**  
[in] Pointer to the object that implementsIMTConSymbolSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTGatewayAPI::SpreadSubscribe](SpreadSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) error is returned.
