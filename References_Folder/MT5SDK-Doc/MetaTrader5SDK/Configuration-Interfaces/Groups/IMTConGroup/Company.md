[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / Company

[Previous](AuthPasswordMin.md) | [Next](CompanyPage.md)

# IMTConGroup::Company

Get the name of the company that services the group.

C++
    
    
    LPCWSTR  IMTConGroup::Company()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.Company()

Python (Manager API)
    
    
    MTConGroup.Company

### Return Value

If successful, it returns a pointer to a string with the name of the company. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGroup](../IMTConGroup.md) object.

# IMTConGroup::Company

Set the name of the company that services the group.

C++
    
    
    MTAPIRES  IMTConGroup::Company(
       LPCWSTR  company      // Company name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.Company(
       string   company      // Company name
       )

Python (Manager API)
    
    
    MTConGroup.Company

### Parameters

**company**  
[in] Name of the company that services the group.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The maximum company name length is 71 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
