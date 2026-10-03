[🏠 Document Start](../README.md) / [Tools](README.md) / CMTArrayBase

[Previous](SMTSearch/SearchRight.md) | [Next](CMTArrayBase/Constructor.md)

# CMTArrayBase

CMTArrayBase is the base class for working with arrays. This class allows you to work with arrays containing any type of data.

In addition to the base class for working with arrays, the MT5APIStorage.h class contains the description of the additional class [TMTArray](CMTArrayBase/Templates.md), which allows to work with typed data arrays. Methods similar to CMTArrayBase methods are used for working with such arrays.

To start working with the arrays using the methods of the CMTArrayBase class, call the [CMTArrayBase::CMTArrayBase()](CMTArrayBase/Constructor.md) constructor and set the size of an element in the array and step of its size change. You can then use the following methods for working with it:

Method | Purpose  
---|---  
[Total](CMTArrayBase/Total.md) | Get the number of elements in the array.  
[Width](CMTArrayBase/Width.md) | Get the size of one entry in the array.  
[Max](CMTArrayBase/Max.md) | Get the maximum number of elements that can be placed in the array without memory reallocation.  
[Step](CMTArrayBase/Step.md) | Get the step of array size change.  
[Compare](CMTArrayBase/Compare.md) | Comparison of the current object with the specified array.  
[Clear](CMTArrayBase/Clear.md) | Clear an array.  
[Zero](CMTArrayBase/Zero.md) | Fill the array with zeros.  
[Shutdown](CMTArrayBase/Shutdown.md) | Free the memory allocated for the array.  
[Compact](CMTArrayBase/Compact.md) | Reallocate an array in a smaller memory block.  
[Assign](CMTArrayBase/Assign.md) | Copy data from the specified array to the current array object.  
[Swap](CMTArrayBase/Swap.md) | Swap the contents of the current array and the contents of the passed array object.  
[Reserve](CMTArrayBase/Reserve.md) | Change the size of the array to the specified number of elements.  
[Resize](CMTArrayBase/Resize.md) | Reserve memory for the specified number of elements in the array.  
[Add](CMTArrayBase/Add.md) | Add elements to an array.  
[AddRange](CMTArrayBase/AddRange.md) | Add a range of elements from the specified array object to the current array object.  
[AddEmpty](CMTArrayBase/AddEmpty.md) | Add empty elements to an array.  
[Append](CMTArrayBase/Append.md) | Add an empty element to an array.  
[Insert](CMTArrayBase/Insert.md) | Insert elements to an array.  
[InsertEmpty](CMTArrayBase/InsertEmpty.md) | insert empty elements at the specified array position.  
[Delete](CMTArrayBase/Delete.md) | Delete elements from an array.  
[DeleteRange](CMTArrayBase/DeleteRange.md) | Delete the range of elements from the array.  
[Remove](CMTArrayBase/Remove.md) | Delete an element taking into account sorting.  
[Update](CMTArrayBase/Update.md) | Update the element at the specified position in the array.  
[Shift](CMTArrayBase/Shift.md) | Shift an element in the array.  
[Trim](CMTArrayBase/Trim.md) | Delete elements from the beginning of the array.  
[Next](CMTArrayBase/Next.md) | Get the array element or a pointer to the array element.  
[Prev](CMTArrayBase/Prev.md) | Get a pointer to the previous array element based on the pointer to the element.  
[At](CMTArrayBase/At.md) | Get a pointer to the array element at the specified position.  
[Position](CMTArrayBase/Position.md) | Get the position of an element in the array based on the pointer to the element.  
[Range](CMTArrayBase/Range.md) | Get the range of elements from the array.  
[Sort](CMTArrayBase/Sort.md) | Sort an array using the sort function passed.  
[Search](CMTArrayBase/Search.md) | Search in an array the array element that matches the search key.  
[SearchGreatOrEq](CMTArrayBase/SearchGreatOrEq.md) | Search in an array the first (from the array beginning) element greater than or equal to the search key.  
[SearchGreater](CMTArrayBase/SearchGreater.md) | Search in an array the first (from the array beginning) element greater than the search key.  
[SearchLessOrEq](CMTArrayBase/SearchLessOrEq.md) | Search in an array the first (from the end) element less than or equal to the search key.  
[SearchLess](CMTArrayBase/SearchLess.md) | Search in an array the first (from the end) element less than the search key.  
[SearchLeft](CMTArrayBase/SearchLeft.md) | Search in an array the first element equal to the search key.  
[SearchRight](CMTArrayBase/SearchRight.md) | Search in an array the last element equal to the search key.
