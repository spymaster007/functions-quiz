# Functions Quiz

## Setup

Open the [Python String page](https://docs.python.org/2/library/string.html).

Fork the repository, then clone your fork.

Disconnect your computer from the internet.

## Quiz

Open `quiz.py`.

Follow this process:

1. Write the code to test a function first!
2. Use the testing code to write the method.
3. Commit with message "Implement method_name"
4. Move on to the next method
5. When all done, verify everything still works and there are no syntax errors.
6. Your quiz **must** define each function, or the grading software will not work. Check that the function names and their number of arguments match the problem declarations exactly.
6. Turn it in with:
    ```$ git push```
7. Have a TA run the grading software and record your results.

## Functions to Implement

1. has_teen

    A number is a teen if it is in the range 13 to 19 inclusive. Given three integers, return true if any of them are a teen.
2. not_string

    Given a string, return a new string where "not" has been added to the front. However, if the string already begins with "not" add the not to the end instead.
3. icy_hot

    It is icy if a temperature is less than zero, and it is hot if a temperature is greater than 100. Given two temperatures, return true if either one is icy and the other is hot.
4. closer_to

    Given a target number and two guesses, return the guess that is closer to the target. If they are the same distance, return 0.
5. two_as_one

    Given three integers, return true if it is possible to add two of the ints to get the third.
6. pig_latinify

    Given a word, return its pig latin conversion. 
    
    Most words in Pig Latin end in "ay." Use the 2 simple rules below to translate normal English into Pig Latin.

    - If a word starts with consonants move the consonants to the end of the word and add "ay."
    
    - If a word starts with a vowel add the word "way" at the end of the word.

    Your code should work for as many english words as possible. I will try to break it! It should also handle some problems with user input:

    - Ignore white space around the original input, so it should return "appleway" for both "apple" and "   apple  ".
    - Ignore case, so it should return "appleway" for both "Apple" and "aPpLe"
    - **Extra Credit** | If a user types in a curse word pig_latinify should censor the result by replacing any vowel in the original word with an asterisk
