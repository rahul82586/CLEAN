[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Custom Functions](../Custom-Functions.md) / CustomCreateStream

[Previous](CustomUnsubscribe.md) | [Next](CustomCommand.md)

# IMTServerAPI::CustomCreateStream

Creation of an object of a byte stream.
    
    
    IMTByteStream*  IMTServerAPI::CustomCreateStream()

### Return Value

It returns a pointer to the created object that implements the [IMTByteStream](../../../Database-Interfaces/Byte-Stream/IMTByteStream.md) interface. In case of failure, it returns NULL.

### Note

The created object must be deleted by calling the [IMTByteStream::Release](../../../Database-Interfaces/Byte-Stream/IMTByteStream/Release.md) method of this object.
