[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / DirectoryRemove

[Previous](DirectoryCreate.md) | [Next](DirectoryClean.md)

# CMTFile::DirectoryRemove

Remove a directory and all its contents.
    
    
    static bool  CMTFile::DirectoryRemove(
       const CMTStr&  path      // Path to the directory
       )

### Parameters

**path**  
[in] Path to the directory that you want to remove.

### Return Value

True if successful, otherwise false.

### Note

Be careful, this method removes a directory and all its contents, including subdirectories.
