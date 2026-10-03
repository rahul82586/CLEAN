[🏠 Document Start](../../../../README.md) / [Gateway API](../../../README.md) / [Main Interface](../../../Main-Interface.md) / [Configuration Databases](../../Configuration-Databases.md) / [Spreads](../Spreads.md) / SpreadAdd

[Previous](SpreadUnsubscribe.md) | [Next](SpreadDelete.md)

# IMTGatewayAPI::SpreadAdd

Add or update a spread configuration.

C++
    
    
    MTAPIRES  IMTGatewayAPI::SpreadAdd(
       IMTSpreadSymbol*  spread      // Spread configuration object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.SpreadAdd(
       CIMTSpreadSymbol  spread      // Spread configuration object
       )

### Parameters

**spread**  
[in] Spread configuration object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is [IMTConSpread::ID](../../../../Configuration-Interfaces/Spreads/IMTConSpread/ID.md). When trying to add a record with an identical ID, no changes are made, and therefore [IMTConSpreadSink::OnSpreadUpdate](../../../../Configuration-Interfaces/Spreads/IMTConSpreadSink/OnSpreadUpdate.md) notification method is not called.
