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

I written a code with Python. Using some binary search algorithm and mathematic method.<br>

This program using about 1-2 minutes to break the hash (Maybe longer if the hash use some large prime number as a key).
Here a short description of what I do.

### Algorithm

1. The task determines the plain text use in NSA encryption is MD5. So, it means the plain text is 32 characters long.
2. Find the lower bound and upper bound number of the key by entering '0000000...' and 'FFFFFF...' (32 characters long) to NSA encryption algorithm as a plain text to find a key.
3. The way to find a key from given plain text using binary search algorithm. For this reason, you get the range of the key.
4. Find factors from the hash string. (I limit the number of factors to  20,000,000 for speed. If the number of factors exceeds 20,000,000 the code will not work [But you can extend it later]. Luckiest, this hash work with factors below 20M :D)
5. Find the divisible number from factors list.
6. Use a number from (6) for find a plain text. (Using binary search again)
7. DONE

## Usage

You can try it by clone this project and run with `python decription.py` (Python 2.7 require [also supported 3.5])
