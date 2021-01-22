//WHILE Loops
let cars = 0;

while (cars) {
    // statements to repeat
  }var a = 0;
  while (a < 5) {
    console.log(a);
    a = a + 1;
  }

//FOR Loops
let dogs = 0;
let cats = 0;
let frogs = 0;

for (dogs; cats; frogs) {
    // statements to repeat
  }for (var i = 0; i < 5; i = i + 1) {
    console.log(i);
  } 

//BREAK Loops
for (var llamas = 4; llamas < 100; llamas++) {
    console.log(llamas + ' Llamas');
    if (llamas % 30 == 0) {
      console.log("That's it! There are " + llamas + " Llamas. Why so many of them!");
      break;
    }
  } 


//Array Length
var rainbowColors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'];
console.log(rainbowColors.length);


//Array Spliting
const myArray = ['h', 'e', 'l', 'l', 'o'];
 
console.log(myArray[0]);
console.log(myArray[1]);


//Array Push
 let toDos = ['eat', 'sleep']; 

 toDos.push('exercise'); 

console.log(toDos);

//Array Unshift
let schedule = ['eat', 'sleep']; 
 
schedule.unshift('work'); 

console.log(schedule); 


//Array Pop

let allDay = ['work', 'eat', 'sleep', 'exercise']; 

allDay.pop();

console.log(allDay);          

const byeBye = allDay.pop();

console.log(byeBye);

console.log(allDay);

//Array Shift

let activities = ['work', 'eat', 'sleep']; 
activities.shift();

 console.log(activities);

