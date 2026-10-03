[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [News Database](../News-Database.md) / NewsBodyRequest

[Previous](NewsNext.md) | [Next](NewsSend.md)

# IMTManagerAPI::NewsBodyRequest

Get the body of the news item received by the manager.

C++
    
    
    MTAPIRES  IMTManagerAPI::NewsBodyRequest(
       const UINT64  id,     // News ID
       IMTNews*      news    // News object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NewsBodyRequest(
       ulong         id,     // News ID
       CIMTNews      news    // News object
       )

Python
    
    
    ManagerAPI.NewsBodyRequest(
       id            # News ID
       )

### Parameters

**pos**  
[in] The ID of the news item received by the manager. TheIMTNews::Idvalue is used as the identifier.

**news**  
[out] News object. The news object must first be created using theIMTManagerAPI::NewsCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method completely fills the 'news' object, i.e. the news body (including attachments), as well as the subject, time, etc.

The method is valid only if the [IMTManagerAPI::PUMP_MODE_NEWS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.

The method cannot be called from event handlers (any methods of IMT*Sink classes).
