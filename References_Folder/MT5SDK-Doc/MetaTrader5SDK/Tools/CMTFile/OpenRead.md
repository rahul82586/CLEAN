[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / OpenRead

[Previous](Open.md) | [Next](OpenWrite.md)

# CMTFile::OpenRead

Open the specified file for reading.
    
    
    bool  CMTFile::OpenRead(
       LPCWSTR  lpFileName      // File name
       )

### Parameters

**lpFileName**  
[in] The name of the file to open.

### Return Value

True if successful, otherwise false.

### Note

This method is similar to [CMTFile::Open](Open.md), but it already contains all the parameters needed to open a file for reading:
