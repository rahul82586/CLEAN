[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / Insert

[Previous](Append.md) | [Next](Copy.md)

# CMTStr::Insert

Add a substring at the specified position of the string object.
    
    
    void  CMTStr::Insert(
       UINT     pos,           // Position
       LPCWSTR  insstring      // Substring
       )

### Parameters

**pos**  
[in] The position in which you want to add a substring. Numbering starts from 0.

**insstring**  
[in] The substring to add.

# CMTStr::Insert

Add a string object at the specified position of another string object.
    
    
    void  CMTStr::Insert(
       UINT          pos,            // Position
       const CMTStr  &insstring      // String object
       )

### Parameters

**pos**  
[in] The position in which you want to add a string object. Numbering starts from 0.

**& insstring**  
[in] TheCMTStrstring object that you want to add.

# CMTStr::Insert

Add a character at the specified position of the string object.
    
    
    void  CMTStr::Insert(
       UINT     pos,         // Position
       wchar_t  inschar      // Character
       )

### Parameters

**pos**  
[in] The position in which you want to add a character. Numbering starts from 0.

**inschar**  
[in] The character that you want to add.
