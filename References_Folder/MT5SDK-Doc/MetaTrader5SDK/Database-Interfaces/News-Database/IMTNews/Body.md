[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [News Database](../../News-Database.md) / [IMTNews](../IMTNews.md) / Body

[Previous](Flags.md) | [Next](BodySize.md)

# IMTNews::Body

Get the news body.

C++
    
    
    LPCVOID  IMTNews::Body()  const

.NET (Gateway/Manager API)
    
    
    byte[]  CIMTNews.Body()

### Return Value

If successful, it returns a pointer to the string with the news body. Otherwise, it returns NULL.

### Note

The returned pointer is valid until the object is deleted by calling Release or another object control method ([IMTNews::Clear](Clear.md)).

# IMTNews::Body

Create the news body.

C++
    
    
    MTAPIRES  IMTNews::Body(
       LPCVOID     body,          // A pointer to the news body
       const UINT  body_size      // The size of the news body
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTNews.Body(
       byte[]      body           // News body
       )

### Parameters

**body**  
[in] A pointer to the news body.

**body_size**  
[in] The size of the news body in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

HTML is supported in newsletter. To send an HTML newsletter, start its body with the <html> tag and end with the </html> tag.
