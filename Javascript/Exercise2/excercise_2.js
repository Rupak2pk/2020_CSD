// Ella Adam    1/7/2021

{
let name = prompt("Enter your first name:");
console.log(name);

let ageString = prompt("How old are you " + name);
console.log(ageString);

let age = Number.parseInt(ageString);

let agey = ++age
let ageStringy = agey.toString();

let str1 ="Hello, "
let str2 = ", in one year your age will be "

let msg = ("Hello, " + name + ", in one year your age will be " + ageStringy);
alert(msg)

} 