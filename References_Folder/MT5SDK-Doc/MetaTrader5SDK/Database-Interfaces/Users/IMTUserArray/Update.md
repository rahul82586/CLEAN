[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTUserArray::Update

Change a client record at the specified position of an array.

C++
    
    
    MTAPIRES  IMTUserArray::Update(
       const UINT  pos,       // Position
       IMTUser*    user       // An object of the client record
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUserArray.Update(
       uint        pos,       // Position
       CIMTUser    user       // An object of the client record
       )

### Parameters

**pos**  
[in] Position of a client record in an array, starting with 0.

**user**  
[in] An object of the client record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTUserArray::Update method deletes the previous element (call of [IMTUser::Release](../IMTUser/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTUserArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTUserArray  *array =api->UserCreateArray();   
       IMTUser       *user1=api->UserCreate();
       IMTUser       *user2=api->UserCreate();
    //---
       array->Add(user1);
       array->Update(0,user2); // The first element (object user1) is replaced by user2
       //--- After that the user1 element will be released using Release, and the user2 lifetime will be controlled by the array
