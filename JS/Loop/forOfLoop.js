let nums = [];
nums[0] = 5;
nums[99] = 9;

console.log(nums.length);

console.log(nums); //[ 5, <98 empty items>, 9 ]

//for in loop
for (key in nums) {
  console.log(nums[key]);
}

//for of loop
for (n of nums) {
  console.log(n);
}

// | Loop Type  | Best For                    | Returns   |
// | ---------- | --------------------------- | --------- |
// | `for...in` | Objects, Arrays             | Key/Index |
// | `for...of` | Arrays, Strings, Sets, Maps | Value     |

let values = ["Vijay", "Swathi"];
for (i in values) {
  console.log(i); // it returns only key or index values only
}
