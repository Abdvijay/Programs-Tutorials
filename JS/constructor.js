function Alien(name, tech) {
  this.name = name;
  this.tech = tech;
  return this;
}

let alien1 = new Alien("Vijay", "JS");
console.log(alien1);

alien1.tech = "CyberSecurity";
console.log(alien1);