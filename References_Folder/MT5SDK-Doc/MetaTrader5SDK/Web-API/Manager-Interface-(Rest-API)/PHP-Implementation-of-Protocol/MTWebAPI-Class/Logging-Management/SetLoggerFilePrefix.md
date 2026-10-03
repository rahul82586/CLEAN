[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Logging Management](../Logging-Management.md) / SetLoggerFilePrefix

[Previous](SetLoggerFilePath.md) | [Next](SetLoggerWriteDebug.md)

# MTWebAPI::SetLoggerFilePrefix

Set a prefix for naming log files.
    
    
    void  MTWebAPI::SetLoggerFilePrefix(
       string  $prefix      // Prefix
       )

### Parameters

**$prefix**  
[in] A prefix for naming log files.

### Note

Log files are named the following way: prefixYYYY_MM_DD.log.
