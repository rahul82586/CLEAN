[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Subject

[Previous](ID.md) | [Next](Category.md)

# IMTNews::Subject

Get the news subject.

C++
    
    
    LPCWSTR  IMTNews::Subject()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTNews.Subject()

### Return Value

If successful, it returns a pointer to a string with the news subject. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTNews](../IMTNews.md) object.

# IMTNews::Subject

Set the news subject.

C++
    
    
    MTAPIRES  IMTNews::Subject(
       LPCWSTR  subject      // News subject
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Subject(
       string   subject      // News subject
       )

### Parameters

**subject**  
[in] News subject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The length of the news subject is not limited.
