[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTPositionArray::AddCopy

Add a copy of an object of a trade position at the end of an array.

C++
    
    
    MTAPIRES  IMTPositionArray::AddCopy(
       const IMTPosition*  position      // The position that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.AddCopy(
       CIMTPosition        position      // The position that is being added
       )

### Parameters

**position**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the position object and places it at the end of the array.

# IMTPositionArray::AddCopy

Add copies of the objects of trade positions in an array.

C++
    
    
    MTAPIRES  IMTPositionArray::AddCopy(
       const IMTPositionArray*  array      // The array of positions that is being added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPositionArray.AddCopy(
       CIMTPositionArray        array      // The array of positions that is being added
       )

### Parameters

**array**  
[in] An object of the array of trade positions.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the objects of positions belonging to the array object, and inserts them at the end of the current array.
