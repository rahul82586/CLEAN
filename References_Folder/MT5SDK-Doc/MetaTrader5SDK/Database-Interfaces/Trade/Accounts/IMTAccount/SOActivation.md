[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccount](../IMTAccount.md) / SOActivation

[Previous](Equity.md) | [Next](SOTime.md)

# IMTAccount::SOActivation

Get the account status as per the minimum amount of funds on the account required to maintain trading positions.

C++
    
    
    UINT  IMTAccount::SOActivation()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTAccount.SOActivation()

### Return Value

A value of the [IMTAccount::EnSoActivation (#ensoactivation)](Enumerations.md#ensoactivation) enumeration.

# IMTAccount::SOActivation

Set the account status as per the minimum amount of funds on the account required to maintain trading positions.

C++
    
    
    MTAPIRES  IMTAccount::SOActivation(
       const UINT  activation      // Account status
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccount.SOActivation(
       uint        activation      // Account status
       )

### Parameters

**activation**  
[in] A value of theIMTAccount::EnSoActivationenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
