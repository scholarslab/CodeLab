# Scholars' Lab Codenundrum no. 0
## Challenge
You are traveling and find a novel bag of Doritos of a variety only available abroad. You desire to taste of its extreme flavor but, as a numismatist, also wish to spend the fewest number of individual units (bills or coins) as possible.

Produce a short bit of code in the modern programing language of your choice that takes as input a set of currency denominations and a target value and returns as output combinations of the fewest units that add up to that value. For example, assuming standard US currency denominations, the expected output for $4.75 is 2,2,0.50,0.25 because those 4 bills/coins constitute the least number that can exactly cover the payment.

Don't assume that the input values will be based on US currency or, in fact, any reasonable real-world currency. I will only guarantee that all values are valid real numbers.

Order does not matter for the output as "1 penny and 1 nickel" is equivalent to "1 nickel and 1 penny". 

If the value cannot be reached with the input denominations, indicate an error. Please document input/output mode (interactive console, file, web form), dependencies, etc.


## Input Format
Input will be provided as a UTF-8 encoded JSON object in the following format:

```javascript
{
"denominations": [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01],
"value": 4.75
}
```

Inputs are guaranteed to be valid JSON.

## Examples (and Hints!)
Here are some example inputs:
```javascript
{
"denominations": [1, 0.75, .01],
"value": 2.50
}
```

```javascript
{
"denominations": [0.01],
"value": 1000.01
}
```

```javascript
{
"denominations": [10000, 0.0000001],
"value": 10000.0000001
}
```

## Scoring
Correctness: 70 points
Edge case handling: 25 points
Speed: 5 points
