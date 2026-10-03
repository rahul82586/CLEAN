[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTStr](../CMTStr.md) / ReplaceChar

[Previous](Replace.md) | [Next](Delete.md)

# CMTStr::ReplaceChar

Replace the specified character in the string object with another character.
    
    
    void  CMTStr::ReplaceChar(
       wchar_t  findchar,     // Character to be replaced
       wchar_t  repchar       // New character
       )

### Parameters

**findchar**  
[in] The character that you want to replace.

**repchar**  
[in] The character that will replace the found characters.

### Note

The method replaces all the characters found.
