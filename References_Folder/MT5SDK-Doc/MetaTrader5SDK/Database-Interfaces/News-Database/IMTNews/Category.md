[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Category

[Previous](Subject.md) | [Next](Time.md)

# IMTNews::Category

Get the news category.

C++
    
    
    LPCWSTR  IMTNews::Category()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTNews.Category()

### Return Value

If successful, it returns a pointer to a string with the news category. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTNews](../IMTNews.md) object. To use the line after the object removal (call of the [IMTNews::Release](Release.md) method of this object), a copy of it should be created.

# IMTNews::Category

Set the news category.

C++
    
    
    MTAPIRES  IMTNews::Category(
       LPCWSTR  category      // Categories
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Category(
       string   category      // Categories
       )

### Parameters

**category**  
[in] News category.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Categories are used for filtering news into [groups](../../../Configuration-Interfaces/Groups.md), and for easy viewing of news in terminals.
