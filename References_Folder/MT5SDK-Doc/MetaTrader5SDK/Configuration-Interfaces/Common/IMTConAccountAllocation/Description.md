[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Description

[Previous](Group.md) | [Next](Flags.md)

# IMTConAccountAllocation::Description

Get the group description displayed in the "Account type" field in client terminals.

C++
    
    
    LPCWSTR  IMTConAccountAllocation::Description()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAccountAllocation.Description()

### Return Value

The method returns a pointer to a string containing the group description on success. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConAccountAllocation](../IMTConAccountAllocation.md) object.

# IMTConAccountAllocation::Description

Set the group description to be displayed in the "Account type" field in client terminals.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::Description(
       LPCWSTR  name      // Group description
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.Description(
       string   name      // Group description
       )

### Parameters

**name**  
[in] Group description.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The group description length is limited to 64 characters (including the end-of-line character). If a string of a greater length is assigned, it will be truncates to the required length.
