let num = 4
console.log(num);

num = 5;
console.log(num);

let userName = "Vijay";
console.log(userName);

//What is let in JavaScript?

//let is used to declare variables in JavaScript. 
//It allows you to create variables with block scope, meaning the variable exists only within the { } where it's defined.

// | Keyword | Scope           | Redeclaration | Reassignment                                |
// | ------- | --------------- | ------------- | ------------------------------------------- |
// | `var`   | Function/Global | Allowed       | Allowed                                     |
// | `let`   | Block Scope     | Not Allowed   | Allowed                                     |
// | `const` | Block Scope     | Not Allowed   | Not Allowed (except objects/arrays content) |

var a = 10;
var a = 20;
console.log(a);

// function test() {
//     if (true) {
//         var x = 10;
//         let y = 20;
//     }
//     console.log(x);  // 10 → var is function-scoped
//     console.log(y); // Error → let is block-scoped
// }
// test();

console.log(p);
var p = 30;

console.log(q);
let q = 10;
