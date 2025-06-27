// File: JS/typeCoercion.js
// This file demonstrates type coercion in JavaScript   
// and how different operations can change the type of a variable.
// It also shows how to use Boolean() for type conversion.
// Type coercion is the automatic or implicit conversion of values from one data type to another.
// JavaScript is a dynamically typed language, meaning variables can hold values of any type and can change types during execution.

let x = 10
console.log(x , typeof x);

x = "8";
console.log(x, typeof x);

x = x + "";
console.log(x, typeof x);

x = x - 2;
console.log(x, typeof x);

console.log(!x, typeof !x);


console.log(Boolean(5), typeof Boolean(5));
console.log(Boolean(0), typeof Boolean(0));

console.log("5" + 2, typeof ("5" + 2)); // String concatenation, results in a string
console.log("5" - 2, typeof ("5" - 2)); // Numeric subtraction, results in a number