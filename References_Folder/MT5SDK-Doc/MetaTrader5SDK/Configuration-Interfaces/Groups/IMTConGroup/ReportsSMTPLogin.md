[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / ReportsSMTPLogin

[Previous](ReportsSMTP.md) | [Next](ReportsSMTPPass.md)

# IMTConGroup::ReportsSMTPLogin

Get a login for the authorization on the SMTP server that is used for sending reports.

C++
    
    
    LPCWSTR  IMTConGroup::ReportsSMTPLogin()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.ReportsSMTPLogin()

Python (Manager API)
    
    
    MTConGroup.ReportsSMTPLogin

### Return Value

If successful, it returns a pointer to a string with login on the SMTP server. Otherwise, it returns NULL.

### Note

The method is obsolete and is no longer used. It always returns an empty line. Please use [IMTConGroup::ReportsEmail](ReportsEmail.md) instead.

To use the string after the object removal (call of the [IMTConGroup::Release](Release.md) method of this object), a copy of it should be created.

# IMTConGroup::ReportsSMTPLogin

Set a login for the authorization on the SMTP server that is used for sending reports.

C++
    
    
    MTAPIRES  IMTConGroup::ReportsSMTPLogin(
       LPCWSTR  login      // Login
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.ReportsSMTPLogin(
       string   login      // Login
       )

Python (Manager API)
    
    
    MTConGroup.ReportsSMTPLogin

### Parameters

**login**  
[in] A login for the authorization on the SMTP server that is used for sending reports.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used. It always returns [MT_RET_OK](../../../Return-Codes/Successful-completion.md). Please use [IMTConGroup::ReportsEmail](ReportsEmail.md) instead.
