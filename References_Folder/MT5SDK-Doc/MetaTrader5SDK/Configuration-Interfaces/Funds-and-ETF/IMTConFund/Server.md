[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / Server

[Previous](SymbolAssets.md) | [Next](Manager.md)

# IMTConFund::Server

Get the identifier of the trade server on which the fund is managed.

C++
    
    
    UINT64  IMTConFund::Server()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.Server()

### Return Value

The identifier of the trade server ([IMTConServer::ID](../../Network/IMTConServer/Id.md))

# IMTConFund::Server

Set the identifier of the trade server on which the fund is managed.

C++
    
    
    MTAPIRES  IMTConFund::Server(
       const UINT64  server      // Server ID
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.Server(
       uint          server      // Server ID
       )

### Parameters

**server**  
[in] The identifier of the trade server (IMTConServer::ID) on which the fund is managed.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
