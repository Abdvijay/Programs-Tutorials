let student1 = {
  tamil: 92,
  english: 84,
  maths: 99,
  science: 100,
  social: 100,
  total: 475,

  compare: function (other) {
    if (this.total > other.total) console.log(this);
    else console.log(other);
  },

  greet: function () {
    console.log(this.total);
  },
};

let student2 = {
  tamil: 87,
  english: 80,
  maths: 98,
  science: 95,
  social: 100,
  total: 460,

  greet: function () {
    console.log(this.total);
  },
};

student1.compare(student2);