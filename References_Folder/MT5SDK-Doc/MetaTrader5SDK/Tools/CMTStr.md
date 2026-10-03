[🏠 Document Start](../README.md) / [Tools](README.md) / CMTStr

[Previous](CMTArrayBase/SearchRight.md) | [Next](CMTStr/Clear.md)

# CMTStr

This class contains additional functions for working with strings. In fact, it is a wrapping of the Unicode string.

To use the methods of the CMTStr class for working with a string, assign it one of the predefined types:

Type | Size  
---|---  
CMTStr16 | 16 characters.  
CMTStr32 | 32 characters.  
CMTStr64 | 64 characters.  
CMTStr128 | 128 characters.  
CMTStr256 | 256 characters.  
CMTStrPath | 260 characters.  
CMTStr512 | 512 characters.  
CMTStr1024 | 1024 characters.  
CMTStr2048 | 2048 characters.  
CMTStr4096 | 4096 characters.  
  
If you need to declare a string with the size differing from the predefined ones, use the TMTStrStatic<xxx> method, where xxx is the size of a string in characters. For example:
    
    
    TMTStrStatic<20> str;

The following methods are available in the CMTStr class:

Method | Purpose  
---|---  
[Clear](CMTStr/Clear.md) | Clear the line. After the execution of this method, the string is empty.  
[Empty](CMTStr/Empty.md) | Check whether the string is empty.  
[Len](CMTStr/Len.md) | Get the length of a string without the end of line character.  
[Max](CMTStr/Max.md) | Get the maximum number of characters that can be placed in the string object.  
[Str](CMTStr/Str.md) | Get a constant pointer to a string.  
[Buffer](CMTStr/Buffer.md) | Get a non-constant pointer to a string.  
[Refresh](CMTStr/Refresh.md) | Update a cached string size after modification.  
[Assign](CMTStr/Assign.md) | Assign a string to an object object.  
[Format](CMTStr/Format.md) | Fill in the string object in accordance with the format string.  
[ToLower](CMTStr/ToLower.md) | Covert characters to lowercase.  
[ToUpper](CMTStr/ToUpper.md) | Covert characters to uppercase.  
[Trim](CMTStr/Trim.md) | Truncate a strung to the specified number of characters.  
[TrimSpaces](CMTStr/TrimSpaces.md) | Remove all space characters from the beginning and end of the string.  
[Replace](CMTStr/Replace.md) | Replace the specified substring in the string object with another substring.  
[ReplaceChar](CMTStr/ReplaceChar.md) | Replace the specified character in the string object with another character.  
[Delete](CMTStr/Delete.md) | Remove a substring from a string.  
[FormatStr](CMTStr/FormatStr.md) | Fill in the specified string in accordance with the format string.  
[Terminate](CMTStr/Terminate.md) | Null the last element (insert end of line character) of the specified string.  
[Append](CMTStr/Append.md) | Add a string/character at the end of a string.  
[Insert](CMTStr/Insert.md) | Add a substring/character in a string.  
[Copy](CMTStr/Copy.md) | Copy strings.  
[CopyCodePage](CMTStr/CopyCodePage.md) | Copy an ANSI string to a Unicode string using the specified code page.  
[Compare](CMTStr/Compare.md) | Compare strings.  
[CompareNoCase](CMTStr/CompareNoCase.md) | Case insensitive comparison of strings.  
[CheckGroupMask](CMTStr/CheckGroupMask.md) | Check the correspondence of a string to the specified mask.  
[Find](CMTStr/Find.md) | Find a substring in a string.  
[FindNoCase](CMTStr/FindNoCase.md) | Case insensitive search of a substring in a string.  
[FindR](CMTStr/FindR.md) | Search for a substring from the end of the string.  
[FindChar](CMTStr/FindChar.md) | Find a character.  
[FindRChar](CMTStr/FindRChar.md) | Search for a character from the end of the string.
