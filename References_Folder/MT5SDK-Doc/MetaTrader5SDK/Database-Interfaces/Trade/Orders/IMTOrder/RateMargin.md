[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrder](../IMTOrder.md) / RateMargin

[Previous](APIDataNext.md) | [Next](ModificationFlags.md)

# IMTOrder::RateMargin

Get the the conversion rate of the [symbol margin currency](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyMargin.md) to the [client's deposit currenc](../../../../Configuration-Interfaces/Groups/IMTConGroup/Currency.md), which is used for calculating the margin for an order.

C++
    
    
    double  IMTOrder::RateMargin()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTOrder.RateMargin()

Python
    
    
    MTOrder.RateMargin()

### Return Value

The exchange rate of the symbol margin currency to the client's deposit currency.

# IMTOrder::RateMargin

Sets the conversion rate of the [symbol margin currency](../../../../Configuration-Interfaces/Symbols/IMTConSymbol/CurrencyMargin.md) to the [client's deposit currency](../../../../Configuration-Interfaces/Groups/IMTConGroup/Currency.md), which is used for calculating the margin for an order.

C++
    
    
    MTAPIRES  IMTOrder::RateMargin(
       const double  rate      // Exchange rate
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTOrder.RateMargin(
       double        rate      // Exchange rate
       )

Python
    
    
    MTOrder.RateMargin()

### Parameters

**rate**  
[in] The exchange rate of the symbol margin currency to the client's deposit currency.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
