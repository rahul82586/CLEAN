[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / Enumerations

[Previous](../IMTComment.md) | [Next](Release.md)

<a id="enumerations"></a>
# Enumerations (#enumerations)

The [IMTComment](../IMTComment.md) interface contains the following enumerations:

  * [IMTComment::EnCommentFlags (#encommentflags)](Enumerations.md#encommentflags)
  * [IMTComment::EnCommentType (#encommenttype)](Enumerations.md#encommenttype)
  * [IMTComment::EnCommentResult (#encommentresult)](Enumerations.md#encommentresult)



<a id="encommentflags"></a>
## IMTComment::EnCommentFlags (#encommentflags)

Comment flags are enumerated in IMTComment::EnCommentFlags:

Identifier | Value | Description  
COMMENT_FLAG_DELETED | 0x1 | Comment was deleted.  
COMMENT_FLAG_IMPORTANT | 0x2 | Comment is marked as important.  
COMMENT_FLAG_NONE | 0 | No flags.  
COMMENT_FLAG_ALL |  | All flags are set.  
  
The enumeration is used in the [IMTComment::Flags](Flags.md) method.

<a id="encommenttype"></a>
## IMTComment::EnCommentType (#encommenttype)

Types of comments are enumerated in IMTComment::EnCommentType:

Identifier | Value | Description  
COMMENT_TYPE_UNDEFINED | 0 | The type is not defined.  
COMMENT_TYPE_LOGRECORD | 1 | Journal based entry.  
COMMENT_TYPE_CALLRECORD | 2 | Call based entry.  
COMMENT_TYPE_ROBOTRECORD | 3 | Automatic entry.  
COMMENT_TYPE_FIRST |  | Enumeration beginning. Corresponds to COMMENT_TYPE_UNDEFINED.  
COMMENT_TYPE_LAST |  | End of enumerationing. Corresponds to COMMENT_TYPE_ROBOTRECORD.  
  
The enumeration is used in the [IMTComment::CommentType](CommentType.md) method.

<a id="encommentresult"></a>
## IMTComment::EnCommentResult (#encommentresult)

Possible results of calling to a client are enumerated in IMTComment::EnCommentResult:

Identifier | Value | Description  
COMMENT_RESULT_UNDEFINED | 0 | Undefined.  
COMMENT_RESULT_CALL_NO_ANSWER | 1 | The call was not answered.  
COMMENT_RESULT_CALL_WRONG_NUMBER | 2 | The phone number is incorrect.  
COMMENT_RESULT_CALL_NOT_INTERESTED | 3 | The client is not interested in the offer.  
COMMENT_RESULT_CALL_SUCCESSFUL | 4 | The call was successful, the client became interested.  
COMMENT_RESULT_FIRST |  | Enumeration beginning. Corresponds to COMMENT_RESULT_UNDEFINED.  
COMMENT_RESULT_LAST |  | End of enumerationing. Corresponds to COMMENT_RESULT_CALL_SUCCESSFUL.  
  
The enumeration is used in the [IMTComment::CommentResult](CommentResult.md) method.
