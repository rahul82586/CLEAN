[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / Size

[Previous](IsOpen.md) | [Next](TimeCreate.md)

# CMTFile::Size

Get the size of the currently open file.
    
    
    UINT64  CMTFile::Size()  const

### Return Value

File size, in bytes.

# CMTFile::Size

Get the size of the specified file.
    
    
    static UINT64  CMTFile::Size(
       LPCWSTR  path      // Path to the file
       )

### Parameters

**path**  
[in] The path to the file, the size of which you want to get.

### Return Value

File size, in bytes.
