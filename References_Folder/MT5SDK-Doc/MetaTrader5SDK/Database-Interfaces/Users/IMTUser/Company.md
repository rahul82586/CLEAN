[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Company

[Previous](MiddleName.md) | [Next](Account.md)

# IMTUser::Company

Get the name of a client's company.

C++
    
    
    LPCWSTR  IMTUser::Company()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Company()

### Return Value

If successful, it returns a pointer to a string with the name of the company. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Company

Set the name of a client's company.

C++
    
    
    MTAPIRES  IMTUser::Company(
       LPCWSTR  id      // Company name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Company(
       sting    id      // Company name
       )

### Parameters

**id**  
[in] The name of a client's company.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the company name is 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
