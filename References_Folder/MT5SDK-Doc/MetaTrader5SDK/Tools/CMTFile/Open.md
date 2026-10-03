[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / Open

[Previous](../CMTFile.md) | [Next](OpenRead.md)

# CMTFile::Open

Open a file.
    
    
    bool  CMTFile::Open(
       LPCWSTR      lpFileName,                             // File name
       const DWORD  dwAccess,                               // Access flags
       const DWORD  dwShare,                                // Share mode
       const DWORD  dwCreationFlags,                        // Types of actions
       const DWORD  dwAttributes=FILE_ATTRIBUTE_NORMAL      // Flags and attributes
       )

### Parameters

**lpFileName**  
[in] The name of the file to open.

**dwAccess**  
[in] File access flags: GENERIC_READ (reading), GENERIC_WRITE (writing) or both flags (GENERIC_READ| GENERIC_WRITE).

**dwShare**  
[in] The sharing mode:

**dwCreationFlags**  
[in] Types of action in case the file exists or does not exist:

**dwAttributes=FILE_ATTRIBUTE_NORMAL**  
[in] Flags and attributes of the file to open. Normally, files are opened with the attribute FILE_ATTRIBUTE_NORMAL, which means that the file has no special attributes.

  * 0 \- prohibits opening of a file when other processes try to delete, read or write the file.
  * FILE_SHARE_DELETE \- allows further opening of the file to delete it.
  * FILE_SHARE_READ \- allows further opening of the file to read it.
  * FILE_SHARE_WRITE \- allows further opening of the file to write it.


  * CREATE_ALWAYS \- always create a new file. If the file that you open exists and it is possible to change it, it will be re-created.
  * CREATE_NEW \- create a new file only if the file to open does not exist.
  * OPEN_ALWAYS \- always open the file. If the file does not exist, the function will create it at a specified location if possible.
  * OPEN_EXISTING \- open the file only if it exists.
  * TRUNCATE_EXISITING \- opens a file and truncates it to zero byte size, but only of the file exists.



### Return Value

True if successful, otherwise false.
