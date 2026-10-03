[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / ChangeSize

[Previous](Seek.md) | [Next](Flush.md)

# CMTFile::ChangeSize

Change the size of the current file to the specified size.
    
    
    bool  CMTFile::ChangeSize(
       const UINT64  size      // Resulting size
       )

### Parameters

**size**  
[in] The final file size in bytes.

### Return Value

True if successful, otherwise false.
