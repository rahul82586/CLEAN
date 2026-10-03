[🏠 Document Start](../../README.md) / [Gateway API](../README.md) / [Event Interface](../Event-Interface.md) / OnGatewayConfig

[Previous](OnServerSymbolDelete.md) | [Next](OnGatewayStart.md)

# IMTGatewaySink::OnGatewayConfig

A handler of the event of passing a gateway own configuration from a history server connected to it.

C++
    
    
    virtual void  IMTGatewaySink::OnGatewayConfig(
       const UINT64         login,       // Login
       const IMTConGateway* config      // Gateway configuration object
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnGatewayConfig(
       ulong                login,       // Login
       CIMTConGateway       config      // Gateway configuration object
       )

### Parameters

**login**  
[in] The login, from which a platform component was connected.

***config**  
[in]The gateway configuration object.

### Note

During the connection a history server passes the gateway settings specified in the platform for it.

  * The symbol settings should not contain the source ([IMTConSymbol::Source](../../Configuration-Interfaces/Symbols/IMTConSymbol/Source.md)). Otherwise, the quotes are copied from it.
  * Receiving quotes from data sources ([IMTConSymbol::TICK_REALTIME (#entickflags)](../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entickflags)) should be enabled in the symbol settings. Otherwise, only quotes thrown in by dealers via the Manager terminals are accepted.
  * The "Quotes" or "Quotes and News" mode ([IMTConFeeder::FEED_FLAG_QUOTES (#enfeedersmode)](../../Configuration-Interfaces/Data-Feeds/IMTConFeeder/Enumerations.md#enfeedersmode)) should be used for a data feed. Otherwise, the data feed quotes are rejected.



# IMTGatewaySink::OnGatewayConfig

A handler of the event of passing a data feed own configuration from a history server connected to it.

C++
    
    
    virtual void  IMTGatewaySink::OnGatewayConfig(
       const UINT64        login,       // Login
       const IMTConFeeder* config       // Data feed configuration object
       )

.NET
    
    
    virtual void  CIMTGatewaySink.OnGatewayConfig(
       ulong               login,       // Login
       CIMTConFeeder       config       // Data feed configuration object
       )

### Parameters

**login**  
[in] The login, from which a platform component was connected.

***config**  
[in]Data feed configuration object.

### Note

History servers of different MetaTrader 5 trading platforms can connect to the same data feed. During the connection a history server passes the data feed settings specified in the platform for it.

  * The symbol settings should not contain the source ([IMTConSymbol::Source](../../Configuration-Interfaces/Symbols/IMTConSymbol/Source.md)). Otherwise, the quotes are copied from it.
  * Receiving quotes from data sources ([IMTConSymbol::TICK_REALTIME (#entickflags)](../../Configuration-Interfaces/Symbols/IMTConSymbol/Enumerations.md#entickflags)) should be enabled in the symbol settings. Otherwise, only quotes thrown in by dealers via the Manager terminals are accepted.
  * The "Trade and Quote" mode (the [IMTConGateway::GATEWAY_FLAG_IGNORE_QUOTES (#engatewaymode)](../../Configuration-Interfaces/Gateways/IMTConGateway/Enumerations.md#engatewaymode) flag is not enabled) should be used for a gateway. Otherwise, the gateway quotes are rejected.


