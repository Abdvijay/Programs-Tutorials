let alien = {
  name: "Vijay",
  lang: "JS",
  laptop: {
    model: "Nitro v",
    ram: "16 GB",
    brand: "Acer",
  },
};

for (let key in alien) {
  if (typeof alien[key] === "object") {
    for(let innerKey in alien[key]){
        console.log(`${innerKey} : ${alien[key][innerKey]}`);
        
    }
  } else {
    console.log(`${key} : ${alien[key]}`);
  }
}

// name : Vijay
// lang : JS
// model : Nitro v
// ram : 16 GB
// brand : Acer