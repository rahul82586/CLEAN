[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Leverages

[Previous](Flags.md) | [Next](Countries.md)

# IMTConAccountAllocation::Leverages

Get the list of available leverage options which can be selected when opening an account in this group.

C++
    
    
    LPCWSTR  IMTConAccountAllocation::Leverages()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAccountAllocation.Leverages()

### Return Value

On success, the method returns a pointer to a string containing a comma-separated list of leverage options. For example: 100,50,30. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConAccountAllocation](../IMTConAccountAllocation.md) object.

# IMTConAccountAllocation::Leverages

Set the list of available leverage options which can be selected when opening an account in this group.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::Leverages(
       LPCWSTR  leverages  // List of leverages
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.Leverages(
       string   leverages  // List of leverages
       )

### Parameters

**leverages**  
[in] Comma-separated list of leverages. For example: 100,50,30.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The length of the list is limited to 64 characters (including the newline character). If a string of a greater length is assigned, it will be truncates to the required length.
