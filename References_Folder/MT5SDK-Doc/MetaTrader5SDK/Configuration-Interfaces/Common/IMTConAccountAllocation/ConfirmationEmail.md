[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConAccountAllocation](../IMTConAccountAllocation.md) / ConfirmationEmail

[Previous](Countries.md) | [Next](AccountAgreementAdd.md)

# IMTConAccountAllocation::ConfirmationEmail

Get the [mail server](../../Mail-Servers/IMTConEmail.md) which will be used for email confirmations when opening accounts in this group.

C++
    
    
    LPCWSTR  IMTConAccountAllocation::ConfirmationEmail()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConAccountAllocation.ConfirmationEmail()

### Return Value

The method returns a pointer to a string with the mail server name on success. Otherwise, NULL is returned.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTConAccountAllocation](../IMTConAccountAllocation.md) object.

To use the string after the object removal (after the call of the [IMTConAccountAllocation::Release](Release.md) method of this object), you should create the string copy.

# IMTConAccountAllocation::ConfirmationEmail

Set the [mail server](../../Mail-Servers/IMTConEmail.md) which will be used for email confirmations when opening accounts in this group.

C++
    
    
    MTAPIRES  IMTConAccountAllocation::ConfirmationEmail(
       LPCWSTR  email      // Mail server
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAccountAllocation.ConfirmationEmail(
       string   email      // Mail server
       )

### Parameters

**email**  
[in] Mail server name. Corresponds toIMTConEmail::Name.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates success. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The length of the list is limited to 64 characters (including the newline character). If a string of a greater length is assigned, it will be truncates to the required length.
