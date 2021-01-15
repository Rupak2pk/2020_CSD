//What number's bigger
function greaterNum(num1, num2) {

if (num1 > num2) {
    return num1;
}

else {
    return num2;
}
}

console.log(greaterNum(5,10));

//The World Translator
function helloWorld(userlang) {
        if (userlang == "German" || userlang == "de") {
            return ("Hallo Welt"); }

        else if (userlang == "Spanish" || userlang == "es") {
            return ("Hola Mundo"); }
        
        else if (userlang == "French" || userlang == "fr") {
            return ("Bonjour le monde"); }

        else {
            return ("Hello World");
        }
    }
console.log(helloWorld("fr"));

//The Grade Assigner
function assignGrade(score) {
    if (score >= 90) {
        return ("You got an A! Fantastic Job!")
    }
    else if (score >= 80) {
        return ("You got an B! Nice Work!")
    }
    else if (score >= 70) {
        return ("You got an C! Congrates!")
    }
    else if (score >= 60) {
        return ("You got an D! Maybe Put More Work In.")
    }
    else{
        return ("You got an F! Come On Man. You Can Do Better!")
    }
}
console.log(assignGrade(95));

//The Pluralizer
function pluralize(noun, num) {
    if (noun != "sheep" && noun != "geese" && num != 1) {
        return (num + " " + noun + "s");
    }

    else {
        return (num + " " + noun);
    }
}

console.log("There are " + pluralize("Horse", 0));
console.log("There are " + pluralize("Horse", 1));
console.log("There are " + pluralize("Horse", 2));