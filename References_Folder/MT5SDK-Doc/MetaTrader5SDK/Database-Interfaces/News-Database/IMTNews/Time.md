[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Time

[Previous](Category.md) | [Next](Language.md)

# IMTNews::Time

Get the time of news sending.

C++
    
    
    INT64  IMTNews::Time()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTNews.Time()

### Return Value

The time of news sending in seconds that have elapsed since 01.01.1970.

# IMTNews::Time

Set the time of news sending.

C++
    
    
    MTAPIRES  IMTNews::Time(
       const INT64  datetime      // Sending time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Time(
       long         datetime      // Sending time
       )

### Parameters

**datetime**  
[in] The time of news sending in seconds that have elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
