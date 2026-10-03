[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Group

[Previous](Clear.md) | [Next](Description.md)

# IMTConAccountAllocation::Group

Get the group in which the accounts requested through terminals will be opened.

C++
    
    
    LPCWSTR  IMTConAccountAllocation::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAccountAllocation.Group()

### Return Value

On success, the method returns a pointer to a string with the group name, including its path. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConAccountAllocation](../IMTConAccountAllocation.md) object.

# IMTConAccountAllocation::Group

Set the group in which the accounts requested through terminals will be opened.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::Group(
       LPCWSTR  name      // Group name
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.Group(
       string   name      // Group name
       )

### Parameters

**name**  
[in] Group name including path.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The group name length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncates to the required length.
