function Alien(name, tech) {
  this.name = name;
  this.tech = tech;

  this.work = function () {
    console.log("Working this mechanishm from 12hrs");
  };
  this.putdata = function () {
    console.log(this.name);
    console.log(this.tech);
  };
}

let alien = new Alien("Vijay", "JS");
alien.putdata();
alien.work();
console.log(alien);