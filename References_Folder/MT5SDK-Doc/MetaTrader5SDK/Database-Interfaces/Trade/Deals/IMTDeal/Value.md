[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Value

[Previous](Profit.md) | [Next](Storage.md)

# IMTDeal::Value

Get the deal value in client deposit currency.

C++
    
    
    double  IMTDeal::Value()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTDeal.Value()

### Return Value

Deal value in client deposit currency

### Note

The rate of conversion to deposit currency is shown in the [IMTDeal::RateMargin](RateMargin.md) field.

# IMTDeal::Value

Set the deal value in client deposit currency.

C++
    
    
    MTAPIRES  IMTDeal::Value(
       const double  value       // value
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Value(
       double        value       // value
       )

### Parameters

**profit**  
[in] Deal value in client deposit currency

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The rate of conversion to deposit currency is shown in the [IMTDeal::RateMargin](RateMargin.md) field.
