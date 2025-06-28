let age = 25;

let hasLicense = true;

if (age >= 18 && hasLicense) {
    console.log("You can drive a car.");
}

let isWeekend = false;
let isHoliday = true;
if (isWeekend || isHoliday) {
    console.log("You can relax today.");
}

// Logical Operators in JavaScript
// And operator truth table
// The `&&` operator is used to combine two or more conditions. It returns true only
// | Expression       | Result  |
// | ---------------- | ------- |
// | `true && true`   | `true`  |
// | `true && false`  | `false` |
// | `false && true`  | `false` |
// | `false && false` | `false` |


// Or operator truth table
// The `||` operator is used to combine two or more conditions. It returns true if
// at least one of the conditions is true.
// | Expression | Result |         |         |
// | ---------- | ------ | ------- | ------- |
// | \`true     |        | true\`  | `true`  |
// | \`true     |        | false\` | `true`  |
// | \`false    |        | true\`  | `true`  |
// | \`false    |        | false\` | `false` |


// Not operator truth table
// The `!` operator is used to negate a boolean value. It returns true if the   
// value is false, and false if the value is true.

// | Expression | Result  |
// | ---------- | ------- |
// | `!true`    | `false` |
// | `!false`   | `true`  |

// ✅ Summary:
// && → Returns true only if both sides are true

// || → Returns true if any one side is true

// ! → Reverses true/false
