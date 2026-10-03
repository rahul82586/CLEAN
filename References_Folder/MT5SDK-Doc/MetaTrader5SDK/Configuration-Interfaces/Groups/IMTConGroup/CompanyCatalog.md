[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CompanyCatalog

[Previous](CompanySupportEmail.md) | [Next](CompanyDepositPage.md)

# IMTConGroup::CompanyCatalog

Get the name of the subdirectory that stores the templates of reports, emails, etc. for the company that services this group.

C++
    
    
    LPCWSTR  IMTConGroup::CompanyCatalog()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.CompanyCatalog()

Python (Manager API)
    
    
    MTConGroup.CompanyCatalog

### Return Value

If successful, it returns a pointer to a string with the name of the templates directory of the company that services this group. Otherwise, it returns NULL.

### Note

The templates subdirectory of the company is located in the standard templates folder of the server.

# IMTConGroup::CompanyCatalog

Set the name of the subdirectory that stores the templates of reports, emails, etc. for the company that services this group.

C++
    
    
    MTAPIRES  IMTConGroup::CompanyCatalog(
       LPCWSTR  catalog      // The name of the templates subdirectory
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CompanyCatalog(
       string   catalog      // The name of the templates subdirectory
       )

Python (Manager API)
    
    
    MTConGroup.CompanyCatalog

### Parameters

**catalog**  
[in] The name of the subdirectory that stores the templates of reports, emails, etc. for the company that services this group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The templates subdirectory of the company is located in the standard templates folder of the server.

The maximum length of the directory name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
