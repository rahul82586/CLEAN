[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFilling](../IMTHistoryFilling.md) / IMTHistoryFilling Comment

[Previous](IMTHistoryFilling-Provider.md) | [Next](../IMTHistoryFillingArray.md)

# IMTECNHistoryFilling::Comment

Get a comment to a filling order.

C++
    
    
    LPCWSTR  IMTECNHistoryFilling::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNHistoryFilling.Comment()

### Return Value

A comment to a filling order.

### Note

A pointer to the resulting string is valid for the [IMTECNMatching](../IMTMatching.md) object lifetime.

To use the string after object deletion (by a call of the [IMTECNFilling::Release](../IMTECNFilling/IMTFilling-Release.md) method of this object), a copy of it should be created.

# IMTECNHistoryFilling

Set a comment to a filling order.

C++
    
    
    MTAPIRES  IMTECNHistoryFilling::Comment(
       LPCWSTR       comment  // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNHistoryFilling.Comment(
       string        comment  // identifier
       )

### Parameters

**comment**  
[in] A comment to a filling order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The symbol name length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
