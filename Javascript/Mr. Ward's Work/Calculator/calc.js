function squareNumber(num) {
    var squaredNumber = num * num;
    console.log(num+ 'Squared' + squaredNumber);
    return squaredNumber;
}

squareNumber(3);

function halfOf(num) {
    var half = num / 2;
    console.log(num + ' Divided equals' + half);
    return half;
}

halfOf(5);

function percentOf(num1, num2) {
    var percent = (num1/num2) * 100;
    console.log(num1 + 'Divided by ' + num2 + 'equals' + percent);
    return percent;
}

percentOf(5,10)

function areaOfCircle(radius) {
    var area = Math.PI * squareNumber(radius);
    console.log(area + 'is the radius of the circle');
    return area;
}

areaOfCircle(2);

function doCrazyStuff(num) {
    var half = halfOf(num);
    var squared = squareNumber(half);
    var area = areaOfCircle(squared);
    var result = percentOf(squared, area);
}

doCrazyStuff(5);
