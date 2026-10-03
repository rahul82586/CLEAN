[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnServerSymbolDelete

[Previous](OnServerSymbolAdd.md) | [Next](OnGatewayConfig.md)

# IMTGatewaySink::OnServerSymbolDelete

A handler of the event of symbol removal.

C++
    
    
    virtual void  IMTGatewaySink::OnServerSymbolDelete(
       LPCWSTR              symbol      // The name of the deleted symbol
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnServerSymbolDelete(
       string               symbol      // The name of the deleted symbol
       )

### Parameters

**config**  
[in] The name of the deleted symbol

### Note

This method is called by the Gateway API to notify the gateway/data feed that a new symbol has been added.

  * If translation is not configured for the deleted symbol, the original name of the symbol used in the platform will be passed.
  * If translation is configured for the deleted symbol, the name of the source symbol is passed in 'symbol'.
  * The IMTGatewaySink::OnServerSymbolDelete method is only called if there are no symbols with the same Source specified in translation settings left in the platform. Consider the following example, 2 symbols are specified in translation settings. EURUSD.1 and EURUSD.2. The two symbols use the same source EURUSD ([IMTConGatewayTranslate::Source](../../Configuration-Interfaces/Gateways/IMTConGatewayTranslate/Source.md)). In this case, the gateway will not receive a notification of OnServerSymbolDelete, until both symbols EURUSD.1 and EURUSD.2 are deleted.


  * The symbol settings should not contain the source ([IMTConSymbol::Source](../../Configuration-Interfaces/Symbols/IMTConSymbol/Source.md)). Otherwise, the quotes are copied from it.
  * Receiving quotes from data sources ([IMTConSymbol::TICK_REALTIME (#entickflags)](../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entickflags)) should be enabled in the symbol settings. Otherwise, only quotes thrown in by dealers via the Manager terminals are accepted.
  * The "Quotes" or "Quotes and News" mode ([IMTConFeeder::FEED_FLAG_QUOTES (#enfeedersmode)](../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Enumerations.md#enfeedersmode)) should be used for a data feed. Otherwise, the data feed quotes are rejected.


  * The "Trade and Quote" mode (the [IMTConGateway::GATEWAY_FLAG_IGNORE_QUOTES (#engatewaymode)](../../Configuration-Interfaces/Gateways/IMTConGateway/Enumerations.md#engatewaymode) flag is not enabled) should be used for a gateway. Otherwise, the gateway quotes are rejected.


