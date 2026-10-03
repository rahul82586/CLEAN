[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeManagementValue

[Previous](FeeManagementType.md) | [Next](FeeManagementAssets.md)

# IMTConFund::FeeManagementValue

Get the fund management fee amount.

C++
    
    
    double  IMTConFund::FeeManagementValue()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConFund.FeeManagementValue()

### Return Value

The fund management fee as a percentage of AUM (Assets Under Management).

# IMTConFund::FeeManagementValue

Set the fund management fee amount.

C++
    
    
    MTAPIRES  IMTConFund::FeeManagementValue(
       const double  fee    // Management fee
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeManagementValue(
       double        fee    // Management fee
       )

### Parameters

**fee**  
[in] The fund management fee as a percentage of AUM (Assets Under Management).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
