[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountDepositURL

[Previous](IMTCon-AccountURL.md) | [Next](IMTCon-AccountWithdrawalURL.md)

# IMTConCommon::AccountDepositURL

Get the URL of the deposit page available for all accounts in the platform.

C++
    
    
    LPCWSTR  IMTConCommon::AccountDepositURL()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.AccountDepositURL()

Python (Manager API)
    
    
    MTConCommon.AccountDepositURL

### Return Value

If successful, the method returns a pointer to a string with the URL address. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConCommon](../IMTCon.md) object.

# IMTConCommon::AccountDepositURL

Set the URL of the deposit page available for all accounts in the platform.

C++
    
    
    MTAPIRES  IMTConCommon::AccountDepositURL(
       LPCWSTR  url      // Deposit page URL
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommon.AccountDepositURL(
       string   url      // Deposit page URL
       )

Python (Manager API)
    
    
    MTConCommon.AccountDepositURL

### Parameters

**url**  
[in] Deposit page URL.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To override the deposit page address for accounts from a specific group, use [IMTConGroup::CompanyDepositPage](../../Groups/IMTConGroup/CompanyDepositPage.md).
