[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon AccountWithdrawalURL

[Previous](IMTCon-AccountDepositURL.md) | [Next](IMTCon-AccountAllocationAdd.md)

# IMTConCommon::AccountWithdrawalURL

Get the URL of the withdrawal page available for all accounts in the platform.

C++
    
    
    LPCWSTR  IMTConCommon::AccountWithdrawalURL()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConCommon.AccountWithdrawalURL()

Python (Manager API)
    
    
    MTConCommon.AccountWithdrawalURL

### Return Value

If successful, the method returns a pointer to a string with the URL address. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConCommon](../IMTCon.md) object.

# IMTConCommon::AccountWithdrawalURL

Set the URL of the withdrawal page for all accounts in the platform.

C++
    
    
    MTAPIRES  IMTConCommon::AccountWithdrawalURL(
       LPCWSTR  url      // Withdrawal page URL
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommon.AccountWithdrawalURL(
       string   url      // Withdrawal page URL
       )

Python (Manager API)
    
    
    MTConCommon.AccountWithdrawalURL

### Parameters

**url**  
[in] Withdrawal page URL.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To override the withdrawal page URL for accounts from a specific group, use [IMTConGroup::CompanyWithdrawalPage](../../Groups/IMTConGroup/CompanyWithdrawalPage.md).
