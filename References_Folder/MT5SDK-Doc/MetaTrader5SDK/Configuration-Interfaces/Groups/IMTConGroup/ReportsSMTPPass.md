[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / ReportsSMTPPass

[Previous](ReportsSMTPLogin.md) | [Next](NewsMode.md)

# IMTConGroup::ReportsSMTPPass

Get a password for the authorization on the SMTP server that is used for sending reports.

C++
    
    
    LPCWSTR  IMTConGroup::ReportsSMTPPass()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.ReportsSMTPPass()

Python (Manager API)
    
    
    MTConGroup.ReportsSMTPPass

### Return Value

If successful, it returns a pointer to a string with a password on the SMTP server. Otherwise, it returns NULL.

### Note

The method is obsolete and is no longer used. It always returns an empty line. Please use [IMTConGroup::ReportsEmail](ReportsEmail.md) instead.

# IMTConGroup::ReportsSMTPPass

Set a password for the authorization on the SMTP server that is used for sending reports.

C++
    
    
    MTAPIRES  IMTConGroup::ReportsSMTPPass(
       LPCWSTR  password      // Password
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.ReportsSMTPPass(
       string   password      // Password
       )

Python (Manager API)
    
    
    MTConGroup.ReportsSMTPPass

### Parameters

**password**  
[in] A password for the authorization on the SMTP server that is used for sending reports.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used. It always returns [MT_RET_OK](../../../Return-Codes/Successful-completion.md). Please use [IMTConGroup::ReportsEmail](ReportsEmail.md) instead.
