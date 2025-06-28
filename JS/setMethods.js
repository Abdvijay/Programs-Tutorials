let num = new Set([1, 2, 3, 4, 5]);
console.log(num);

num.add(100);
console.log(num);

num.delete(100);
console.log(num);

console.log(num.size);

console.log(num.values());

console.log(num.has(100));

// | Method           | Action                |
// | ---------------- | --------------------- |
// | `.add(value)`    | Add new unique value  |
// | `.delete(value)` | Remove specific value |
// | `.has(value)`    | Check if value exists |
// | `.size`          | Get total count       |
// | `.clear()`       | Remove all values     |