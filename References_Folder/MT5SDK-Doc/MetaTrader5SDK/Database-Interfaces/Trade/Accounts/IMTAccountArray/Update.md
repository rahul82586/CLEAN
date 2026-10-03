[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTAccountArray::Update

Changes a trading account at the specified position of an array.

C++
    
    
    MTAPIRES  IMTAccountArray::Update(
       const UINT     pos,       // Position
       IMTAccount*    user        // An object of a trading account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Update(
       uint           pos,       // Position
       CIMTAccount    user       // An object of a trading account
       )

### Parameters

**pos**  
[in] Position of the trading account in an array, starting with 0.

**user**  
[in] Trading account object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTAccountArray::Update method deletes the previous element (call of [IMTAccount::Release](../IMTAccount/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTAccountArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTAccountrArray  *array =api->UserCreateArray();   
       IMTAccount        *account1=api->UserCreateAccount();
       IMTAccount        *account2=api->UserCreateAccount();
    //---
       array->Add(account1);
       array->Update(0,account2); // The first element (object account1) is replaced by account2
       //--- After that the account1 element will be released using Release, and the account2 lifetime will be controlled by the array
