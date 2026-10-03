[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTAccountArray::AddCopy

Adds a copy of an object of a trading account at the end of an array.

C++
    
    
    MTAPIRES  IMTAccountArray::AddCopy(
       const IMTAccount*  account      // Account to add
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.AddCopy(
       CIMTAccount        account      // Account to add
       )

### Parameters

**account**  
[in] Trading account object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'account' object and places it at the end of the array.

# IMTAccountArray::AddCopy

Adds copies of the objects of client records to an array.

C++
    
    
    MTAPIRES  IMTAccountArray::AddCopy(
       const IMTAccountArray*  array      // An array of trading accounts that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.AddCopy(
       CIMTAccountArray        array      // An array of trading accounts that is being added
       )

### Parameters

**array**  
[in] An object of the array of trading accounts.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates copies of objects of trading accounts belonging to the 'array' object, and inserts them at the end of the current array.
