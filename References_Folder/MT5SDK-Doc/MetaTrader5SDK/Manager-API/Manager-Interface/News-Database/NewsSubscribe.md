[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [News Database](../News-Database.md) / NewsSubscribe

[Previous](NewsCreate.md) | [Next](NewsUnsubscribe.md)

# IMTManagerAPI::NewsSubscribe

Subscribe to events and hooks associated with changes in the news database.

C++
    
    
    MTAPIRES  IMTManagerAPI::NewsSubscribe(
       IMTNewsSink*  sink      // A pointer to the IMTNewsSink object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.NewsSubscribe(
       CIMTNewsSink  sink      // CIMTNewsSink object
       )

Python
    
    
    ManagerAPI.NewsSubscribe(
       sink          # IMTNewsSink object
       )

### Parameters

**sink**  
[in] A pointer to the object that implements theIMTNewsSinkinterface.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Subscribing to events is thread safe. One and the same interface [IMTNewsSink](../../../Database-Interfaces/News-Database/IMTNewsSink.md) cannot subscribe to an event twice - in this case the response code [MT_RET_ERR_DUPLICATE](../../../Return-Codes/Common-errors.md) is returned.
