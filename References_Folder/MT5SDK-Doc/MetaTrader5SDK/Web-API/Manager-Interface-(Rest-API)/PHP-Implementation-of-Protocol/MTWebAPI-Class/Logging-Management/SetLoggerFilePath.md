[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Logging Management](../Logging-Management.md) / SetLoggerFilePath

[Previous](SetLoggerIsWrite.md) | [Next](SetLoggerFilePrefix.md)

# MTWebAPI::SetLoggerFilePath

Set the path to the folder where you want to place the log files.
    
    
    void  MTWebAPI::SetLoggerFilePath(
       string  $file_path      // Path to files
       )

### Parameters

**$file_path**  
[in] Path to the directory where the log files will be created.

### Note

Permissions to write information to the specified folder are required.
