[🏠 Document Start](../README.md) / [Tools](README.md) / CMTFile

[Previous](SMTTime/Sec.md) | [Next](CMTFile/Open.md)

<a id="cmtfile"></a>
# CMTFile (#cmtfile)

This class contains additional functions for working with files.

Method | Purpose  
---|---  
[Open](CMTFile/Open.md) | Open a file.  
[OpenRead](CMTFile/OpenRead.md) | Open the specified file for reading.  
[OpenWrite](CMTFile/OpenWrite.md) | Open the specified file for writing.  
[Close](CMTFile/Close.md) | Close the previously opened file.  
[Handle](CMTFile/Handle.md) | Get the handle (Windows descriptor) of a file, with which you can work using the appropriate WinAPI methods.  
[IsOpen](CMTFile/IsOpen.md) | Check whether there is an open file (file handle).  
[Size](CMTFile/Size.md) | Get the file size.  
[TimeCreate](CMTFile/TimeCreate.md) | Get the creation time of the currently open file.  
[TimeLastAccess](CMTFile/TimeLastAccess.md) | Get the time of the last access to the currently open file.  
[TimeLastModify](CMTFile/TimeLastModify.md) | Get the time of the last modification of the currently open file.  
[CurrPos](CMTFile/CurrPos.md) | Get the current position in the open file.  
[Read](CMTFile/Read.md) | Reading from a currently open file.  
[Write](CMTFile/Write.md) | Write to the currently open file.  
[Seek](CMTFile/Seek.md) | Move the pointer of the current position in a file.  
[ChangeSize](CMTFile/ChangeSize.md) | Change the size of the current file to the specified size.  
[Flush](CMTFile/Flush.md) | Forced writing of data from the file cache to disk.  
[FilesCopy](CMTFile/FilesCopy.md) | Copy files from one directory to another  
[DirectoryCreate](CMTFile/DirectoryCreate.md) | Create a directory.  
[DirectoryRemove](CMTFile/DirectoryRemove.md) | Remove a directory and all its contents.  
[DirectoryClean](CMTFile/DirectoryClean.md) | Delete files from a specified directory based on the file mask.  
  
<a id="constants"></a>
## Constants (#constants)

The following constants are used in the class:

Constant | Value  
---|---  
INVALID_POSITION | _UI64_MAX
