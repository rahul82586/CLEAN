[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTPositionArray::Update

Change a trade position at the specified index of an array.

C++
    
    
    MTAPIRES  IMTPositionArray::Update(
       const UINT    pos,          // Position index
       IMTPosition*  position      // Position object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.Update(
       uint          pos,          // Position index
       CIMTPosition  position      // Position object
       )

### Parameters

**pos**  
[in] The index of a trade position in an array, starting with 0.

**position**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTPositionArray::Update method deletes the previous element (call of [IMTPosition::Release](../IMTPosition/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTPositionArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- Example
       IMTPositionArray *array    =api->PositionCreateArray();   
       IMTPosition      *position1=api->PositionCreate();
       IMTPosition      *poistion2=api->PositionCreate();
    //---
       array->Add(position1);
       array->Update(0,position2); // The first element (object position1) is replaced by position2
       //--- After that the position1 element will be released using Release, and the position2 lifetime will be controlled by the array
