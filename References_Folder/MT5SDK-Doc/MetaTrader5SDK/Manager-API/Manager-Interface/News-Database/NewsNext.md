[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [News Database](../News-Database.md) / NewsNext

[Previous](NewsTotal.md) | [Next](NewsBodyRequest.md)

# IMTManagerAPI::NewsNext

Get the news item received by the manager.

C++
    
    
    MTAPIRES  IMTManagerAPI::NewsNext(
       const UINT  pos,      // News position
       IMTNews*    news      // News object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NewsNext(
       uint        pos,      // News position
       CIMTNews    news      // News object
       )

Python
    
    
    ManagerAPI.NewsNext(
       pos         # News position
       )

### Parameters

**pos**  
[in] Position of the news item received by the manager, ranging from 0.

**news**  
[out] News object. The news object must first be created using theIMTManagerAPI::NewsCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method copies data of the news item at the specified position to the news object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_NEWS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
