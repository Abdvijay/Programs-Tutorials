// | Method       | Action                |
// | ------------ | --------------------- |
// | `.set(k, v)` | Add key-value pair    |
// | `.get(k)`    | Get value by key      |
// | `.has(k)`    | Check if key exists   |
// | `.delete(k)` | Remove pair by key    |
// | `.size`      | Total number of pairs |
// | `.clear()`   | Remove all pairs      |

let map = new Map();

//1.add to a map
map.set("Name", "Vijay");
map.set("Age", 24);
map.set("Tech", "JS");

console.log(map); //Map(3) { 'Name' => 'Vijay', 'Age' => 24, 'Tech' => 'JS' }

//2.get from a map
console.log(map.get("Name")); //Vijay
console.log(map.get("Tech")); //JS

//3.Delete in a map
map.delete("Age");
console.log(map); //Map(2) { 'Name' => 'Vijay', 'Tech' => 'JS' }

//4.Size of a map
console.log(map.size);

//5.has on a map
console.log(map);
console.log(map.has("Name"));
console.log(map.has("Age"));

//6.keys on a map
console.log(map.keys()); //[Map Iterator] { 'Name', 'Tech' }

//7.values on a map
console.log(map.values()); //[Map Iterator] { 'Vijay', 'JS' }

//8.for of loop on a map
for (let [key, value] of map) {
  console.log(`${key} : ${value}`);
}
// Name : Vijay
// Tech : JS

//9. foreach on a map
map.forEach((value, key) => {
  console.log(`${key} : ${value}`);
});
// Name : Vijay
// Tech : JS
map.forEach(function (value, key) {
  console.log(`${key} : ${value}`);
});
// Name : Vijay
// Tech : JS
