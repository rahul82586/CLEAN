[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / OpenWrite

[Previous](OpenRead.md) | [Next](Close.md)

# CMTFile::OpenWrite

Open the specified file for writing.
    
    
    bool  CMTFile::OpenWrite(
       LPCWSTR  lpFileName      // File name
       )

### Parameters

**lpFileName**  
[in] The name of the file to open.

### Return Value

True if successful, otherwise false.

### Note

This method is similar to [CMTFile::Open](Open.md), but it already contains all the parameters needed to open a file for writing:
