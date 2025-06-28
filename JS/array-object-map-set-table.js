// | Feature        | **Array**              | **Object**                            | **Map**                         | **Set**                           |
// | -------------- | ---------------------- | ------------------------------------- | ------------------------------- | --------------------------------- |
// | **Stores**     | Ordered list of values | Key-value pairs (keys mostly strings) | Key-value pairs (keys any type) | Unique values only                |
// | **Duplicates** | Allowed                | Keys must be unique                   | Keys must be unique             | No duplicates                     |
// | **Add**        | `push()` or `index`    | `obj.key = value`                     | `map.set(key, value)`           | `set.add(value)`                  |
// | **Update**     | Assign by index        | `obj.key = newValue`                  | `map.set(key, newValue)`        | Remove & re-add (if needed)       |
// | **Delete**     | `splice()` or `pop()`  | `delete obj.key`                      | `map.delete(key)`               | `set.delete(value)`               |
// | **Size**       | `.length`              | `Object.keys().length`                | `.size`                         | `.size`                           |
// | **Access**     | By index               | By key                                | By key                          | By looping or check with `.has()` |
// | **Iteration**  | `for`, `forEach`, etc. | `for...in`, `Object.keys()`           | `for...of`, `.forEach()`        | `for...of`, `.forEach()`          |

let arr = [1, 2, 3];

// Add
arr.push(4);

// Update
arr[0] = 10;

// Delete
arr.splice(1, 1);  // Remove element at index 1

// Display
console.log(arr);  // [10, 3, 4]

// Size
console.log(arr.length);  // 3


let obj = { name: "Vijay", age: 25 };

// Add
obj.city = "Chennai";

// Update
obj.age = 26;

// Delete
delete obj.name;

// Display
console.log(obj);  // { age: 26, city: "Chennai" }

// Size
console.log(Object.keys(obj).length);  // 2

let map = new Map();

// Add
map.set("name", "Vijay");
map.set(1, "One");

// Update
map.set("name", "Vijay Kumar");

// Delete
map.delete(1);

// Display
console.log(map);  // Map { 'name' => 'Vijay Kumar' }

// Size
console.log(map.size);  // 1

let set = new Set();

// Add
set.add(5);
set.add(10);
set.add(5);  // Duplicate ignored

// Delete
set.delete(10);

// Display
console.log(set);  // Set { 5 }

// Size
console.log(set.size);  // 1
