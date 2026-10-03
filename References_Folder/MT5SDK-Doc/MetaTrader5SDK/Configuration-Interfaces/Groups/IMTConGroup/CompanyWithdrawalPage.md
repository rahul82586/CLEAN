[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CompanyWithdrawalPage

[Previous](CompanyDepositPage.md) | [Next](Currency.md)

# IMTConGroup::CompanyWithdrawalPage

Get the withdrawal page URL set for a group of accounts.

C++
    
    
    LPCWSTR  IMTConGroup::CompanyWithdrawalPage()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.CompanyWithdrawalPage()

Python (Manager API)
    
    
    MTConGroup.CompanyWithdrawalPage

### Return Value

If successful, the method returns a pointer to a string with the URL address. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConCommon](../../Common/IMTCon.md) object.

# IMTConGroup::CompanyWithdrawalPage

Set the URL of the withdrawal page for accounts from the specific group.

C++
    
    
    MTAPIRES  IMTConGroup::CompanyWithdrawalPage(
       LPCWSTR  url      // Withdrawal page URL
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CompanyWithdrawalPage(
       string   url      // Withdrawal page URL
       )

Python (Manager API)
    
    
    MTConGroup.CompanyWithdrawalPage

### Parameters

**url**  
[in] Withdrawal page URL.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To set the withdrawal page URL for all accounts in the platform, use [IMTConCommon::AccountWithdrawalURL](../../Common/IMTConCommon/IMTCon-AccountWithdrawalURL.md). The priority of group settings is higher and they override global setting.
