[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTFile](../CMTFile.md) / TimeLastModify

[Previous](TimeLastAccess.md) | [Next](CurrPos.md)

# CMTFile::TimeLastModify

Get the time of the last modification of the currently open file.
    
    
    FILETIME  CMTFile::TimeLastModify()  const

### Return Value

File modification time in the FILETIME format - a 64-bit value representing the number of 100-nanosecond intervals since January 1, 1601. (UTC).
