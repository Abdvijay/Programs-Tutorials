//Mon - 7am
//Tue - Thu - 8am
//Fri - 7.30am
//Sat - Sun - 9am

let day = "Tuesday"
switch(day){
    case "Monday" : console.log("Alarm : 7am"); break;
    case "Friday" : console.log("Alarm : 7.30am"); break;
    case "Saturday": console.log("Alarm : 9am"); break;
    case "Sunday": console.log("Alarm : 9am"); break;
    default: console.log("Alarm : 8am");
}