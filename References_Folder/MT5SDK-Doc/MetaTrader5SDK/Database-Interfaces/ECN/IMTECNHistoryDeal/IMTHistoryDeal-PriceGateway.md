[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal PriceGateway

[Previous](IMTHistoryDeal-Price.md) | [Next](IMTHistoryDeal-Digits.md)

# IMTECNHistoryDeal::PriceGateway

Get the price at which the deal was actually executed on the external system side.

C++
    
    
    double  IMTECNHistoryDeal::PriceGateway()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNHistoryDeal.PriceGateway()

### Return Value

The price at which the deal was actually executed on the external system side.

# IMTECNHistoryFilling::PriceGateway

Set the price at which the deal was actually executed on the external system side.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::PriceGateway(
       const double  price      // deal price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.PriceGateway(
       double        price      // deal price
       )

### Parameters

**price**  
[in] The price at which the deal was actually executed on the external system side.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
