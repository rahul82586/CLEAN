[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [News Event](../News-Event.md) / NewsSend

[Previous](../News-Event.md) | [Next](../Prices.md)

# MT5WebAPI.NewsSend

Send news via the internal news system of the platform.
    
    
    MTRetCode  MT5WebAPI.NewsSend(
       string          subject,         // Subject
       string          category,        // Category
       uint            language,        // News language
       int             priority,        // Priority
       string          text             // News text
       )

### Parameters

**subject**  
[in] News subject.

**category**  
[in] News category. To specify a subcategory use a backlash "\". For example, "Economy\World".

**language**  
[in] News language in the LANGID format used inMS Windows(value from Prim.lang.identifier). The zero value means that the news has no language binding.

**priority**  
[in] Priority news. 0 — normal news, 1 — high-priority.

**text**  
[in] News body. You may use HTML to format news.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
