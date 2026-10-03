[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTExecution](../Requests-IMTExecution.md) / Requests DealCommission

[Previous](Requests-DealStorage.md) | [Next](Requests-Position.md)

# IMTExecution::DealCommission

Gets the commission charged when conducting deals via a gateway in an external trading system.

C++
    
    
    double  IMTExecution::DealCommission()  const

.NET (Gateway/Manager API)C++
    
    
    double  CIMTExecution.DealCommission()

### Return Value

Commission amount. A negative value means funds are deducted from the account. A positive value means funds are added to the account.

# IMTExecution::DealCommission

Sets the commission charged when conducting deals via a gateway in an external trading system.

C++
    
    
    MTAPIRES  IMTExecution::DealCommission(
       const double  comm      // Commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTExecution.DealCommission(
       double        comm      // Commission
       )

### Parameters

**comm**  
[in] Commission amount in the group deposit currency. A negative value means funds are deducted from the account. A positive value means funds are added to the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

After applying a trade execution with the specified commission, the commission amount is immediately debited from the client's account. The amount of charged commission is recorded in the IMTDeal::Commission field of the appropriate deal.
