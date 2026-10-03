[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [News Database](../News-Database.md) / NewsUnsubscribe

[Previous](NewsSubscribe.md) | [Next](NewsTotal.md)

# IMTManagerAPI::NewsUnsubscribe

Undubscribe from events and hooks associated with changes in the news database.

C++
    
    
    MTAPIRES  IMTManagerAPI::NewsUnsubscribe(
       IMTNewsSink*  sink      // A pointer to the IMTNewsSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NewsUnsubscribe(
       CIMTNewsSink  sink      // CIMTNewsSink object
       )

Python
    
    
    ManagerAPI.NewsUnsubscribe(
       sink          # IMTNewsSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTNewsSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This is a pair method to [IMTManagerAPI::NewsSubscribe](NewsSubscribe.md). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) error is returned.
