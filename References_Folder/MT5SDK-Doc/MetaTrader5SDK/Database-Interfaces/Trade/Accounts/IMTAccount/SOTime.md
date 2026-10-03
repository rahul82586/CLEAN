[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / SOTime

[Previous](SOActivation.md) | [Next](SOLevel.md)

# IMTAccount::SOTime

Get the time when the Margin Call or Stop Out level was reached.

C++
    
    
    INT64  IMTAccount::SOTime()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTAccount.SOTime()

### Return Value

The time when the Margin Call or Stop Out level was reached , in seconds that had elapsed since 01.01.1970. If the current equity is above these levels, 0 is returned.

# IMTAccount::SOTime

Set the time when the Margin Call or Stop Out level was reached.

C++
    
    
    MTAPIRES  IMTAccount::SOTime(
       const INT64  datetime      // SO or MC reaching time
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.SOTime(
       long         datetime      // SO or MC reaching time
       )

### Parameters

**datetime**  
[in] The time when the Margin Call or Stop Out level was reached , in seconds that had elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
