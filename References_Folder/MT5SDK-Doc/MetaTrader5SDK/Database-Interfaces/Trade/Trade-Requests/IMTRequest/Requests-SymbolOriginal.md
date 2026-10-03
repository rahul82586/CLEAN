[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequest](../Requests-IMTRequest.md) / Requests SymbolOriginal

[Previous](Requests-Symbol.md) | [Next](Requests-Digits.md)

# IMTRequest::SymbolOriginal

Get the original symbol in a trade request received by the Gateway API.

C++
    
    
    LPCWSTR  IMTRequest::SymbolOriginal()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTRequest.SymbolOriginal()

### Return Value

If successful, returns a pointer to a string with the original request symbol. Otherwise, NULL is returned.

### Note

The method is used only in the Gateway API. The value is filled in the [IMTGatewaySink::OnDealerLock](../../../../Gateway-API/Event-Interface/OnDealerLock.md) event.

  * IMTRequest::SymbolOriginal — original symbol name on the MetaTrader 5 side.
  * [IMTRequest::Symbol](Requests-Symbol.md) — symbol name for the external system translated in accordance with the gateway translation settings.



# IMTRequest::SymbolOriginal

Set the original symbol in a trade request received by the Gateway API.

C++
    
    
    MTAPIRES  IMTRequest::SymbolOriginal(
       LPCWSTR  symbol      // Symbol
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTRequest.SymbolOriginal(
       string   symbol      // Symbol
       )

### Parameters

**symbol**  
[in] The original symbol of the trade request.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code has occurred.

### Note

The method is used only in the Gateway API.
