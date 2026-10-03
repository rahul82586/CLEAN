[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CompanyEmail

[Previous](CompanyPage.md) | [Next](CompanySupportPage.md)

# IMTConGroup::CompanyEmail

Get the email address of the company that services the group.

C++
    
    
    LPCWSTR  IMTConGroup::CompanyEmail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.CompanyEmail()

Python (Manager API)
    
    
    MTConGroup.CompanyEmail

### Return Value

If successful, it returns a pointer to a string with the email address of the company. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGroup](../IMTConGroup.md) object.

# IMTConGroup::CompanyEmail

Set the email address of the company that services the group.

C++
    
    
    MTAPIRES  IMTConGroup::CompanyEmail(
       LPCWSTR  email      // Email address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CompanyEmail(
       string   email      // Email address
       )

Python (Manager API)
    
    
    MTConGroup.CompanyEmail

### Parameters

**email**  
[in] The email address of the company that services the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the email address is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
