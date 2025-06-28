let alien = {
    name : 'Vijay',
    tech : 'JS',
    'home loc' : 'Banglore'
}
console.log(alien) //{ name: 'Vijay', tech: 'JS', 'home loc': 'Banglore' }
console.log(alien.name) // Vijay
console.log(alien['home loc']) // Banglore

alien['age'] = 45;
alien.country = "India"
console.log(alien);