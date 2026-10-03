[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Funds and ETF](../../Funds-and-ETF.md) / [IMTConFund](../IMTConFund.md) / FeeManagementType

[Previous](FeeAccount.md) | [Next](FeeManagementValue.md)

# IMTConFund::FeeManagementType

Get the type of fund management fee.

C++
    
    
    UINT  IMTConFund::FeeManagementType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConFund.FeeManagementType()

### Return Value

The type of fund management fee.

### Note

The method is currently not used.

# IMTConFund::FeeManagementType

Set the type of fund management fee.

C++
    
    
    MTAPIRES  IMTConFund::FeeManagementType(
       const UINT  fee      // Type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConFund.FeeManagementType(
       uint        fee      // Type
       )

### Parameters

**fee**  
[in] The type of fund management fee.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method is currently not used.
