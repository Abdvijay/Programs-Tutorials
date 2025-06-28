let x = 6;
let y = 4;

console.log(x > y);  // true
console.log(x < y);  // false
console.log(x >= y); // true
console.log(x <= y); // false
console.log(x == y); // false
console.log(x != y); // true
console.log(x === y); // false (strict equality, checks value and type)
console.log(x !== y); // true (strict inequality, checks value and type)

let x1 = "6";
let y1 = 6;

console.log(x1 == y1);  // true (loose equality, type coercion occurs)
console.log(x1 === y1); // false (strict equality, no type coercion)

let x2 = false;
let y2 = 0;
console.log(x2 == y2);  // true (loose equality, false is coerced to 0)
console.log(x2 === y2); // false (strict equality, different types)