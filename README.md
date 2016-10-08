# Code2040TechFellowshipApp
Step III: Needle in a haystack

Next, let’s check your skills for working with collections.

We’re going to send you a dictionary with two values and keys. The first value, needle, is a string. The second value, haystack, is an array of strings. You’re going to tell the API where the needle is in the array.

Grab that dictionary from here, again by POSTing your token:

http://challenge.code2040.org/api/haystack

Locate the needle in the haystack array. You’re going to send back the position, or “index,” of the needle string. The API expects indexes to start counting at 0.

POST your results to:

http://challenge.code2040.org/api/haystack/validate

Use the key token for your token.

Use the key needle for the integer representing where the needle was in the array.

Hint: You’ll probably use a loop to solve this one.
