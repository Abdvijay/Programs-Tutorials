let alien = {
    name : 'Vijay',
    lang : 'JS',
    laptop : {
        model : 'Nitro v',
        ram : '16 GB',
        brand : 'Acer',
    },
}
console.log(alien);
/*
{
  name: 'Vijay',
  lang: 'JS',
  laptop: { model: 'Nitro v', ram: '16 GB', brand: 'Acer' }
}
*/

console.log(alien.laptop); //{ model: 'Nitro v', ram: '16 GB', brand: 'Acer' }

console.log(alien.laptop.brand); //Acer

console.log(alien.laptop1?.brand.length) //undefined

delete alien.laptop.ram
console.log(alien);

/*
{
  name: 'Vijay',
  lang: 'JS',
  laptop: { model: 'Nitro v', brand: 'Acer' }
}
*/