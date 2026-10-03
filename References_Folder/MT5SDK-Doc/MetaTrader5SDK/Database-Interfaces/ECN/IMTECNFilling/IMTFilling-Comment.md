[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFilling](../IMTFilling.md) / IMTFilling Comment

[Previous](IMTFilling-Provider.md) | [Next](../IMTFillingArray.md)

# IMTECNFilling::Comment

Get a comment to a filling order.

C++
    
    
    LPCWSTR  IMTECNFilling::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTECNFilling.Comment()

### Return Value

A comment to a filling order.

### Note

A pointer to the resulting string is valid for the [IMTECNMatching](../IMTMatching.md) object lifetime.

# IMTECNFilling::Comment

Set a comment to a filling order.

C++
    
    
    MTAPIRES  IMTECNFilling::Comment(
       LPCWSTR       comment  // identifier
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTECNFilling.Comment(
       string        comment  // identifier
       )

### Parameters

**comment**  
[in] A comment to a filling order.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

The comment length is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to the specified length.
