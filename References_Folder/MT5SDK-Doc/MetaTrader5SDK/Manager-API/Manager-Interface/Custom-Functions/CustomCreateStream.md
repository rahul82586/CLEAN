[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Custom Functions](../Custom-Functions.md) / CustomCreateStream

[Previous](CustomCommand.md) | [Next](../ECN.md)

# IMTManagerAPI::CustomCreateStream

Creation of an object of a byte stream.

C++
    
    
    IMTByteStream*  IMTManagerAPI::CustomCreateStream()

.NET
    
    
    CIMTByteStream  CIMTManagerAPI.CustomCreateStream()

### Return Value

It returns a pointer to the created object that implements the [IMTByteStream](../../../Database-Interfaces/Byte-Stream/IMTByteStream.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTByteStream::Release](../../../Database-Interfaces/Byte-Stream/IMTByteStream/Release.md) method of this object.
