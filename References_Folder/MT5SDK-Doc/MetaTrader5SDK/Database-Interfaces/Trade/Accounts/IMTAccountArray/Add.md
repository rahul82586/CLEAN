[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTAccountArray::Add

Adds an object of a trading account at the end of an array.

C++
    
    
    MTAPIRES  IMTAccountArray::Add(
       IMTAccount*  account      // Account to add
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Add(
       CIMTAccount  account      // Account to add
       )

### Parameters

**account**  
[in] Trading account object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the 'account' object is passed to the array object. Thus, when deleting an array object (call of [IMTAccountArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTAccountArray::Add

Adds an array of objects of trading accounts at the end of the array.

C++
    
    
    MTAPIRES  IMTAccountArray::Add(
       IMTAccountArray*  array      // An array of trading accounts that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAccountArray.Add(
       CIMTAccountArray  array      // An array of trading accounts that is being added
       )

### Parameters

**array**  
[in] An object of the array of trading accounts.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.

### Example
    
    
    //--- Example
       IMTAccountArray *array=api->UserCreateAccountArray();   
       IMTAccount      *account=api->UserCreateAccount();
    //---
       array->Add(account);  // After that the lifetime is controlled by an array
       array->Delete(0);     // Delete the first element, and the pointer in order becomes invalid (Release was called)
     
    //--- An example of incorrect use
       IMTAccountArray  *array=api->UserCreateAccountArray();   
       IMTAccount       *account=api->UserCreateAccount();
    //---
       array->Add(account);
       array->Add(account); // In this case the array contains two pointers to the same object!
       //--- Releasing the object will cause crash, because it will try to delete an object twice
