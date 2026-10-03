[🏠 Document Start](../../README.md) / [Tools](../README.md) / [CMTArrayBase](../CMTArrayBase.md) / Templates

[Previous](Constructor.md) | [Next](Total.md)

# Templates

In addition to the base class for working with arrays, the MT5APIStorage.h class contains the description of the additional class [TMTArray](Templates.md), which allows to work with typed data arrays. Methods similar to [CMTArrayBase](../CMTArrayBase.md) methods are used for working with such arrays.

To start using the methods for working with arrays, declare an array object through a template:
    
    
    TMTArray<T,step> arr;

Two parameters are specified for the array:

  * T — the type of data that will be stored in the array.
  * step — the array change step for reallocation of memory for the array. The step is specified as a number of elements.



Then you can work with the array using the methods similar to the methods of class [CMTArrayBase](../CMTArrayBase.md) by calling them as methods of the TMTArray class. For example, a method similar to [CMTArrayBase::Add](Add.md) will be used as follows:
    
    
    bool  TMTArray::Add(
       const T  *elem      // An element to be added
       )

The type of data earlier set for the array will be used as the type of the element to add.
