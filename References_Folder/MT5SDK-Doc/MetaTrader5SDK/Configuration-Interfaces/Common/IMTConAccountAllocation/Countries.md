[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / Countries

[Previous](Leverages.md) | [Next](ConfirmationEmail.md)

# IMTConAccountAllocation::Countries

Get the list of countries in which it will be possible to open an account in this group.

C++
    
    
    LPCWSTR  IMTConAccountAllocation::Countries()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAccountAllocation.Countries()

### Return Value

In case of success, the method returns a pointer to a string containing a comma-separated list of two-letter country codes. For example: US,CY,ES. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConAccountAllocation](../IMTConAccountAllocation.md) object.

To use the string after the object removal (after the call of the [IMTConAccountAllocation::Release](Release.md) method of this object), you should create the string copy.

# IMTConAccountAllocation::Countries

Set the list of countries in which it will be possible to open an account in this group.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::Countries(
       LPCWSTR  countries  // List of countries
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.Countries(
       string   countries  // List of countries
       )

### Parameters

**leverages**  
[in] A comma-separated list of two-letter country codes. For example: US,CY,ES. Specify 'All' to include all countries.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The length of the list is limited to 64 characters (including the newline character). If a string of a greater length is assigned, it will be truncates to the required length.
