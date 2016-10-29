# NSA Encryption Puzzle Breaker

This is the breaker for NSA encryption puzzle.

I found a task from Facebook page name [สอนแฮกเว็บแบบแมวๆ](https://www.facebook.com/longhackz/photos/a.1560357644219017.1073741828.1559669844287797/1753068201614626/) (It's a really good page :D)

The objective of the task.

1. Read the encryption code (look the code below)
2. You got the long hash string without know the exactly key and plain text.
3. Find the key and plain text and decrypt the plain text with MD5.

## Task

Follow the original task here [https://gist.github.com/anonymous/7d19a35c54e7dac40fa1a470df4a209a](https://gist.github.com/anonymous/7d19a35c54e7dac40fa1a470df4a209a)

```php
<?php
/**
* Encrypts a given plaintext using the supplied key.
*
* @param  key  		a numeric key with a value greater than 255
* @param  plainText  	a string containing the plaintext you want to encrypt
*
* @return number   	a unique number for this given key and plaintext
*/
function nsaEncrypt($key, $plainText)
{ 
	$result = 0;
	for ($character = 0; $character < strlen($plainText); $character++)
	{
		$result = bcadd($result, ord($plainText[$character]));
		$result = bcmul($result, $key);
	}
	return $result;
}
```

## Solution

I written a code with Python. Using some binary search algorithm and mathmatic method.<br>
You can ask me directly if you need some more information.

You can try it by clone this project and run with `python decription.py` (Python 2.7 require [also supported 3.5])
