[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Commission

[Previous](Storage.md) | [Next](Fee.md)

# IMTDeal::Commission

Get the amount of commission charged for a deal.

C++
    
    
    double  IMTDeal::Commission()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.Commission()

### Return Value

The amount of commission charged for a deal. A negative value means funds are deducted from the account. A positive value means funds are added to the account.

# IMTDeal::Commission

Set the amount of commission for a deal.

C++
    
    
    MTAPIRES  IMTDeal::Commission(
       const double  comm      // Commission
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Commission(
       double        comm      // Commission
       )

### Parameters

**comm**  
[in] Commission for a deal. A negative value means funds are deducted from the account. A positive value means funds are added to the account.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
