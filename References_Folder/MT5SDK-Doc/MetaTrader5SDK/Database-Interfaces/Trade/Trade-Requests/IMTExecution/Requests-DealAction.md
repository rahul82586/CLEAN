[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealAction

[Previous](Requests-DealExternalID.md) | [Next](Requests-DealVolume.md)

# IMTExecution::DealAction

Get the type (direction) of a deal.

C++
    
    
    UINT  IMTExecution::DealAction()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTExecution.DealAction()

### Return Value

Deal direction - IMTDeal::DEAL_BUY or IMTDeal::DEAL_SELL.

# IMTExecution::DealAction

Set the type (direction) of a deal.

C++
    
    
    MTAPIRES  IMTExecution::DealAction(
       const UINT  action      // Deal type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealAction(
       uint        action      // Deal type
       )

### Parameters

**action**  
[in] Deal type (direction) - IMTDeal::DEAL_BUY or IMTDeal::DEAL_SELL

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
