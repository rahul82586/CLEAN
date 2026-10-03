[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTConfirm](../Requests-IMTConfirm.md) / Requests ExternalRetcode

[Previous](Requests-PriceGateway.md) | [Next](../Requests-IMTExecution.md)

# IMTConfirm::ExternalRetcode

Gets the code of response from an external trading system.

C++
    
    
    int  IMTConfirm::ExternalRetcode()  const

.NET (Gateway/Manager API)
    
    
    int  CIMTConfirm.ExternalRetcode()

### Return Value

Response code.

### Note

It is used to provide extended information about the operation execution result on the exchange. For example, it allows you to find out the reason for order rejection. On the client terminal side, the response code can be obtained using MqlTradeResult.external_retcode in MQL5.

# IMTConfirm::ExternalRetcode

Sets the code of response from an external trading system.

C++
    
    
    MTAPIRES  IMTConfirm::ExternalRetcode(
       const int    retcode  // Response code
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConfirm.ExternalRetcode(
       int          retcode  // Response code
       )

### Parameters

**id**  
[in] Response code.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

It is used to provide extended information about the operation execution result on the exchange. For example, it allows you to find out the reason for order rejection. On the client terminal side, the response code can be obtained using MqlTradeResult.external_retcode in MQL5.
