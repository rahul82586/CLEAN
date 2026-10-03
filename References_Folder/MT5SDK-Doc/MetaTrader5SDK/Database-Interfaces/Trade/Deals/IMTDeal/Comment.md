[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDeal](../IMTDeal.md) / Comment

[Previous](PositionID.md) | [Next](ApiDataSet.md)

# IMTDeal::Comment

Get a comment to a deal.

C++
    
    
    LPCWSTR  IMTDeal::Comment()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTDeal.Comment()

### Return Value

If successful, it returns a pointer to a string with a comment to a deal. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTDeal](../IMTDeal.md) object.

# IMTDeal::Comment

Set a comment to a deal.

C++
    
    
    MTAPIRES  IMTDeal::Comment(
       LPCWSTR  comment      // Comment
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDeal.Comment(
       string   comment      // Comment
       )

### Parameters

**comment**  
[in] A comment to the deal.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the comment is limited to 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.
