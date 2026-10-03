[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / CompanySupportPage

[Previous](CompanyEmail.md) | [Next](CompanySupportEmail.md)

# IMTConGroup::CompanySupportPage

Get the website address of the technical support of the company that services the group.

C++
    
    
    LPCWSTR  IMTConGroup::CompanySupportPage()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.CompanySupportPage()

Python (Manager API)
    
    
    MTConGroup.CompanySupportPage

### Return Value

If successful, it returns a pointer to a string with the company's technical support website address. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGroup](../IMTConGroup.md) object.

# IMTConGroup::CompanySupportPage

Set the website address of the technical support of the company that services the group.

C++
    
    
    MTAPIRES  IMTConGroup::CompanySupportPage(
       LPCWSTR  page      // Website address
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.CompanySupportPage(
       string   page      // Website address
       )

Python (Manager API)
    
    
    MTConGroup.CompanySupportPage

### Parameters

**page**  
[in] The technical support website address of the company that manages the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the website address is 256 characters (with the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.
