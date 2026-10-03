[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Byte Stream](../Byte-Stream.md) / IMTByteStream

[Previous](../Byte-Stream.md) | [Next](IMTByteStream/Release.md)

# IMTByteStream

The interface is designed to represent the byte stream. It enables transmission of raw byte values.The interface provides for an easier operation with transmitted data, because all the required memory operations are implemented in the interface and are hidden from the user.

> Each IMTByteStream object can only be used for data reading (Read methods), or for data writing (Add methods).

Method | Purpose  
---|---  
[Release](IMTByteStream/Release.md) | Delete the current object.  
[Assign](IMTByteStream/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTByteStream/Clear.md) | Clear an object.  
[Len](IMTByteStream/Len.md) | Gets the length of the stream object in bytes.  
[ReadLen](IMTByteStream/ReadLen.md) | Gets the current amount of data read from the stream object.  
[Add](IMTByteStream/Add.md) | Adds data to the stream object.  
[AddChar](IMTByteStream/AddChar.md) | Adds Char data to the stream object.  
[AddUChar](IMTByteStream/AddUChar.md) | Adds UChar data to the stream object.  
[AddShort](IMTByteStream/AddShort.md) | Adds Short data to the stream object.  
[AddUShort](IMTByteStream/AddUShort.md) | Adds UShort data to the stream object.  
[AddInt](IMTByteStream/AddInt.md) | Adds Int data to the stream object.  
[AddUInt](IMTByteStream/AddUInt.md) | Adds UInt data to the stream object.  
[AddInt64](IMTByteStream/AddInt64.md) | Adds Int64 data to the stream object.  
[AddUInt64](IMTByteStream/AddUInt64.md) | Adds UInt64 data to the stream object.  
[AddFloat](IMTByteStream/AddFloat.md) | Adds Float data to the stream object.  
[AddDouble](IMTByteStream/AddDouble.md) | Adds Double data to the stream object.  
[AddResult](IMTByteStream/AddResult.md) | Adds MTAPIRES data to the stream object.  
[AddStr](IMTByteStream/AddStr.md) | Adds String data to the stream object.  
[ReadReset](IMTByteStream/ReadReset.md) | Resets the read pointer of the stream object to the beginning.  
[Read](IMTByteStream/Read.md) | Reads data from the stream object.  
[ReadSkip](IMTByteStream/ReadSkip.md) | Moves the read pointer by the specified number of bytes.  
[ReadChar](IMTByteStream/ReadChar.md) | Reads Char data from the stream object.  
[ReadUChar](IMTByteStream/ReadUChar.md) | Reads UChar data from the stream object.  
[ReadShort](IMTByteStream/ReadShort.md) | Reads Short data from the stream object.  
[ReadUShort](IMTByteStream/ReadUShort.md) | Reads UShort data from the stream object.  
[ReadInt](IMTByteStream/ReadInt.md) | Reads Int data from the stream object.  
[ReadUInt](IMTByteStream/ReadUInt.md) | Reads UInt data from the stream object.  
[ReadInt64](IMTByteStream/ReadInt64.md) | Reads Int64 data from the stream object.  
[ReadUInt64](IMTByteStream/ReadUInt64.md) | Reads UInt64 data from the stream object.  
[ReadFloat](IMTByteStream/ReadFloat.md) | Reads Float data from the stream object.  
[ReadDouble](IMTByteStream/ReadDouble.md) | Reads Double data from the stream object.  
[ReadResult](IMTByteStream/ReadResult.md) | Reads MTAPIRES data from the stream object.  
[ReadStr](IMTByteStream/ReadStr.md) | Reads String data from the stream object.  
The web methods described below are only used for the MetaTrader 5 Server API.  
[WebAddParamStr](IMTByteStream/WebAddParamStr.md) | Adds a String parameter to the stream object for transmission to a web client.  
[WebAddParamChar](IMTByteStream/WebAddParamChar.md) | Adds a Char parameter to the stream object for transmission to a web client.  
[WebAddParamUChar](IMTByteStream/WebAddParamUChar.md) | Adds a UChar parameter to the stream object for transmission to a web client.  
[WebAddParamShort](IMTByteStream/WebAddParamShort.md) | Adds a Short parameter to the stream object for transmission to a web client.  
[WebAddParamUShort](IMTByteStream/WebAddParamUShort.md) | Adds a UShort parameter to the stream object for transmission to a web client.  
[WebAddParamInt](IMTByteStream/WebAddParamInt.md) | Adds an Int parameter to the stream object for transmission to a web client.  
[WebAddParamUInt](IMTByteStream/WebAddParamUInt.md) | Adds a UInt to the stream object for transmission to a web client.  
[WebAddParamInt64](IMTByteStream/WebAddParamInt64.md) | Adds an Int64 parameter to the stream object for transmission to a web client.  
[WebAddParamUInt64](IMTByteStream/WebAddParamUInt64.md) | Adds a UInt64 parameter to the stream object for transmission to a web client.  
[WebAddParamDouble](IMTByteStream/WebAddParamDouble.md) | Adds a Double parameter to the stream object for transmission to a web client.  
[WebAddParamFinalize](IMTByteStream/WebAddParamFinalize.md) | Completes the formation of parameters of the command sent in response to a web client.  
[WebReadCommand](IMTByteStream/WebReadCommand.md) | Reads the command sent by a web client.  
[WebReadParamName](IMTByteStream/WebReadParamName.md) | Reads the name of the next parameter of the command sent by a web client.  
[WebReadParamStr](IMTByteStream/WebReadParamStr.md) | Reads the value of a String parameter from the command sent by a web client.  
[WebReadParamSkip](IMTByteStream/WebReadParamSkip.md) | Skips parameter value. After calling this method, moves to the name of the next parameter.  
[WebReadParamChar](IMTByteStream/WebReadParamChar.md) | Reads the value of a Char parameter from the command sent by a web client.  
[WebReadParamUChar](IMTByteStream/WebReadParamUChar.md) | Reads the value of a UChar parameter from the command sent by a web client.  
[WebReadParamShort](IMTByteStream/WebReadParamShort.md) | Reads the value of a Short parameter from the command sent by a web client.  
[WebReadParamUShort](IMTByteStream/WebReadParamUShort.md) | Reads the value of a UShort parameter from the command sent by a web client.  
[WebReadParamInt](IMTByteStream/WebReadParamInt.md) | Reads the value of an Int parameter from the command sent by a web client.  
[WebReadParamUInt](IMTByteStream/WebReadParamUInt.md) | Reads the value of a UInt parameter from the command sent by a web client.  
[WebReadParamInt64](IMTByteStream/WebReadParamInt64.md) | Reads the value of an Int64 parameter from the command sent by a web client.  
[WebReadParamUInt64](IMTByteStream/WebReadParamUInt64.md) | Reads the value of a UInt64 parameter from the command sent by a web client.  
[WebReadParamDouble](IMTByteStream/WebReadParamDouble.md) | Reads the value of a Double parameter from the command sent by a web client.
