[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / NewsCategory

[Previous](NewsMode.md) | [Next](NewsLangAdd.md)

# IMTConGroup::NewsCategory

Get the categories of news received by the group.

C++
    
    
    LPCWSTR  IMTConGroup::NewsCategory()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTConGroup.NewsCategory()

Python (Manager API)
    
    
    MTConGroup.NewsCategory

### Return Value

If successful, it returns a pointer to a string with the categories of news received by the group. The zero value means that the group receives all news irrespective of the categories. Otherwise, it returns NULL.

# IMTConGroup::NewsCategory

Set the categories of news received by the group.

C++
    
    
    MTAPIRES  IMTConGroup::NewsCategory(
       LPCWSTR  category      // News categories
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.NewsCategory(
       string   category      // News categories
       )

Python (Manager API)
    
    
    MTConGroup.NewsCategory

### Parameters

**category**  
[in] Categories of news separated by commas.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The maximum length of the categories list is 64 characters (with the sign of the string end). If a string of a greater length is assigned, then the group will receive all news irrespective of the category. The zero value also means that the group will receive all news categories.
