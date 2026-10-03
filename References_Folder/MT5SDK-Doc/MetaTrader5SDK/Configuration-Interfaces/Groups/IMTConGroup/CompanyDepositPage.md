[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CompanyDepositPage

[Previous](CompanyCatalog.md) | [Next](CompanyWithdrawalPage.md)

# IMTConGroup::CompanyDepositPage

Get the deposit page URL set for a group of accounts.

C++
    
    
    LPCWSTR  IMTConGroup::CompanyDepositPage()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.CompanyDepositPage()

Python (Manager API)
    
    
    MTConGroup.CompanyDepositPage

### Return Value

If successful, the method returns a pointer to a string with the URL address. Otherwise, NULL is returned.

### Note

A pointer to the resulting string is valid for the lifetime of the [IMTConCommon](../../Common/IMTCon.md) object.

# IMTConGroup::CompanyDepositPage

Set the URL of the deposit page available for accounts from the specific group.

C++
    
    
    MTAPIRES  IMTConGroup::CompanyDepositPage(
       LPCWSTR  url      // Deposit page URL
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CompanyDepositPage(
       string   url      // Deposit page URL
       )

Python (Manager API)
    
    
    MTConGroup.CompanyDepositPage

### Parameters

**url**  
[in] Deposit page URL.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

To set the deposit page URL for all accounts in the platform, use [IMTConCommon::AccountDepositURL](../../Common/IMTConCommon/IMTCon-AccountDepositURL.md). The priority of group settings is higher and they override global setting.
