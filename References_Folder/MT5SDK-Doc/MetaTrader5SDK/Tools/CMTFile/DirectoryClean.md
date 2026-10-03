[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / DirectoryClean

[Previous](DirectoryRemove.md) | [Next](../../Development-Features/README.md)

# CMTFile::DirectoryClean

Delete files from a specified directory based on the file mask.
    
    
    static bool  CMTFile::DirectoryClean(
       const CMTStr&  path,     // Path to the directory
       const CMTStr&  mask      // Mask of files
       )

### Parameters

**path**  
[in] The path to the directory, from which you want to delete files.

**mask**  
[in] The mask of the files to delete. For example, *.dat. Use of mask *.*,deletes all files and subdirectories.

### Return Value

True if successful, otherwise false.
