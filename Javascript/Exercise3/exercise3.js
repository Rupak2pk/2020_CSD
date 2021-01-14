fullName ={
    first: "Ella", 
    last: "Adam",
    print() {

        msg = "Hello, " + this.first + " " + this.last + "\n";
		msg+= "Let me shout it! \n";
        msg+= this.first.toUpperCase() + " " + this.last.toUpperCase();
        alert(msg);}
}

let inputFName = prompt("Enter your first name:");

if (inputFName.length ==0) {
    msg = ("No name entered. Using Default");
    alert(msg);
}

else {
    fullName.first = inputFName;
}

let inputLName = prompt("Enter your last name:");

if (inputLName.length ==0) {
    msg = ("No name entered. Using Default");
    alert(msg);
}

else {
    fullName.last = inputLName;
}



fullName.print();