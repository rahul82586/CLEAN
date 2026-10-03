[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / Seek

[Previous](Write.md) | [Next](ChangeSize.md)

# CMTFile::Seek

Move the pointer of the current position in a file.
    
    
    UINT64  CMTFile::Seek(
       const INT64  distance,     // Distance
       const DWORD  method        // Method of moving
       )

### Parameters

**distance**  
[in] When using the FILE_BEGIN or FILE_END methods - the new position of the pointer from the file beginning or end, respectively.

**method**  
[in] The method of moving the pointer of the current position in a file:

  * FILE_BEGIN \- the zero position (file beginning) is used as the initial point.
  * FILE_CURRENT \- the current position is used as the initial point.
  * FILE_END \- the file end is used as the initial point.



### Return Value

If successful, returns a new position. In case of an error returns [INVALID_POSITION (#constants)](../CMTFile.md#constants).

### 
