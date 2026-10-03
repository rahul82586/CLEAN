[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / DemoDeposit

[Previous](DemoLeverage.md) | [Next](DemoInactivityPeriod.md)

# IMTConGroup::DemoDeposit

Gets the default amount of deposit set for demo accounts opened in the group.

C++
    
    
    double  IMTConGroup::DemoDeposit()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConGroup.DemoDeposit()

Python (Manager API)
    
    
    MTConGroup.DemoDeposit

### Return Value

The default amount of deposit for demo accounts opened in the group.

# IMTConGroup::DemoDeposit

Set the default amount of deposit for demo accounts opened in the group.

C++
    
    
    MTAPIRES  IMTConGroup::DemoDeposit(
       const double  deposit      // Default deposit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.DemoDeposit(
       double        deposit      // Default deposit
       )

Python (Manager API)
    
    
    MTConGroup.DemoDeposit

### Parameters

**deposit**  
[in] The default amount of deposit for demo accounts opened in the group.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
