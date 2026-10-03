[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / MaxCapital

[Previous](EndDate.md) | [Next](Currency.md)

# IMTConFund::MaxCapital

Get the maximum allowable investment amount for a fund.

C++
    
    
    double  IMTConFund::MaxCapital()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConFund.MaxCapital()

### Return Value

The maximum allowable investment amount for a fund.

### Note

The currency in which the amount is specified, is determined by the [IMTConFund::Currency](Currency.md) property.

# IMTConFund::MaxCapital

Set the maximum allowable investment amount for a fund.

C++
    
    
    MTAPIRES  IMTConFund::MaxCapital(
       const double  max_capital  // Investment amount
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.MaxCapital(
       double        max_capital  // Investment amount
       )

### Parameters

**max_capital**  
[in] The maximum allowable investment amount for a fund.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The currency in which the amount is specified, is determined by the [IMTConFund::Currency](Currency.md) property.
