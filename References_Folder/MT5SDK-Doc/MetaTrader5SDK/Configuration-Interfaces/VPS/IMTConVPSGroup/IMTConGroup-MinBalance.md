[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSGroup](../IMTConGroup.md) / IMTConGroup MinBalance

[Previous](IMTConGroup-Group.md) | [Next](IMTConGroup-InactiveDays.md)

# IMTConVPSGroup::MinBalance

Get the minimum balance a trader should have on the account to be able to use the sponsored VPS.

C++
    
    
    double  IMTConVPSGroup::MinBalance()  const

.NET (Gateway/Manager API)
    
    
    double  CIMTConVPSGroup.MinBalance()

Python
    
    
    MTConVPSGroup.MinBalance

### Return Value

If successful, the method returns a pointer to a string with the currency name. Otherwise, it returns NULL.

### Note

The setting is specified for each group.

# IMTConVPSGroup::MinBalance

Set the minimum balance a trader should have on the account to be able to use the sponsored VPS.

C++
    
    
    MTAPIRES  IMTConVPSGroup::MinBalance(
       double   balance   // minimum balance in USD
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSGroup.MinBalance(
       double   balance   // minimum balance in USD
       )

Python
    
    
    MTConVPSGroup.MinBalance

### Parameters

**balance**  
[in] Minimum balance on the trader's account in USD.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The setting is specified for each group.
