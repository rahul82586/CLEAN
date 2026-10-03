[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Delete

[Previous](ReplaceChar.md) | [Next](FormatStr.md)

# CMTStr::Delete

Delete a substring of the specified length from a string object, starting at the specified position (character).
    
    
    void  CMTStr::Delete(
       UINT  pos,     // Position
       UINT  len      // Number of characters
       )

### Parameters

**pos**  
[in] The position starting from which the specified number of characters should be deleted. Numbering starts from 0.

**len**  
[in] The number of characters to delete.

# CMTStr::Delete

Delete a substring of the specified length from the specified string, starting at the specified position (character).
    
    
    static void  CMTStr::Delete(
       wchar_t  (&dst)[dstsize],     // String
       UINT     pos,                 // Position
       UINT     len                  // Number of characters
       )

### Parameters

**( &dst)[dstsize]**  
[in][out] The string, from which you want to delete a substring (a pointer to the dst buffer of the dstsize size).

**pos**  
[in] The position starting from which the specified number of characters should be deleted. Numbering starts from 0.

**len**  
[in] The number of characters to delete.

### Note

To use this method, the compiler must know the size of the string buffer.

# CMTStr::Delete

Delete a substring of the specified length from the specified string, starting at the specified position (character).
    
    
    static void  CMTStr::Delete(
       LPWSTR  dst,         // String
       UINT    dstsize,     // Size
       UINT    pos,         // Position
       UINT    len          // Number of characters
       )

### Parameters

**dst**  
[in][out] A pointer to a Unicode string, from which you want to delete a substring.

**dstsize**  
[in] The size of the dst buffer in characters.

**pos**  
[in] The position starting from which the specified number of characters should be deleted. Numbering starts from 0.

**len**  
[in] The number of characters to delete.

### Note

In this method, the size of the string buffer is explicitly specified.
