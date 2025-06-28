let alien = {
  name: "Vijay",
  tech: "JS",
  "home loc": "Banglore",
};
console.log(alien); //{ name: 'Vijay', tech: 'JS', 'home loc': 'Banglore' }
console.log(alien.name); // Vijay
console.log(alien["home loc"]); // Banglore

alien["age"] = 45;
alien.country = "India";
console.log(alien);

alien.age = 24;
console.log(alien);

delete alien["home loc"];
console.log(alien);
