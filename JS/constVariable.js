let radius = 5
const pi = 3.14

radius = 10; // This will throw an error because 'radius' is declared with 'let' and can be reassigned
//pi = 3.14159; // This will throw an error because 'pi' is declared with 'const' and cannot be reassigned
// TypeError: Assignment to constant variable.

// Calculate the area of a circle
let area = pi * radius * radius 
console.log("The area of the circle is: " + area);

// | Keyword | Scope           | Redeclaration | Reassignment | Modify Contents (Objects/Arrays) |
// | ------- | --------------- | ------------- | ------------ | -------------------------------- |
// | `var`   | Function/Global | Allowed       | Allowed      | Allowed                          |
// | `let`   | Block Scope     | Not Allowed   | Allowed      | Allowed                          |
// | `const` | Block Scope     | Not Allowed   | Not Allowed  | Allowed                          |
