[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / TimeLastAccess

[Previous](TimeCreate.md) | [Next](TimeLastModify.md)

# CMTFile::TimeLastAccess

Get the time of the last access to the currently open file.
    
    
    FILETIME  CMTFile::TimeLastAccess()  const

### Return Value

The time of the last access in the FILETIME format - a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601. (UTC).
