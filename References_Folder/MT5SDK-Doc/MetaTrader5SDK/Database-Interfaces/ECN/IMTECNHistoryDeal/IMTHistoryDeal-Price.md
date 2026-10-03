[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDeal](../IMTHistoryDeal.md) / IMTHistoryDeal Price

[Previous](IMTHistoryDeal-VolumeExt.md) | [Next](IMTHistoryDeal-PriceGateway.md)

# IMTECNHistoryDeal::Price

Get the price at which the deal was executed on the platform side.

C++
    
    
    double  IMTECNHistoryDeal::Price()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTECNHistoryDeal.Price()

### Return Value

The price at which the deal was executed on the platform side.

### Note

The price is passed taking into account [translation settings (#general)](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_translation#general).

# IMTECNHistoryFilling::Price

Set the price at which the deal was executed on the platform side.

C++
    
    
    MTAPIRES  IMTECNHistoryDeal::Price(
       const double  price      // deal price
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryDeal.Price(
       double        price      // deal price
       )

### Parameters

**price**  
[in] The price at which the deal was executed on the platform side.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
