// CHANGE PICTURE
// document.getElementById("demo").innerHTML = "Hello JavaScript";

function change(){
    document.getElementById("img1").src="images/img2.png";
    document.getElementById("img2").src="images/img1.png";
    document.innewrite("Javascript has taken effect!");
    alert("CHANGED!");
}

// CALCULATOR
const num1_input = document.getElementById('num1');
const num2_input = document.getElementById('num2');
const result_field = document.getElementById('result');

function getNum1(){
    return parseFloat(num1_input.value);
}
function getNum2(){
    return parseFloat(num2_input.value);
}

function add(x, y){
    let result = x + y;
    return result 

}

function subtract(x, y){
    let result = x - y;
    return result 

}

function divide(x, y){
    let result = x / y;
    return result 

}

function multiply(x, y){
    let result = x * y;
    return result 

}

function modulus(x, y){
    let result = x % y;
    return result 

}

function addClick(){
    let x = getNum1();
    let y = getNum2();
    let result = add(x, y)
    result_field.value = result
}

function subtractClick(){
    let x = getNum1();
    let y = getNum2();
    let result = subtract(x, y)
    result_field.value = result
}

function divideClick(){
    let x = getNum1();
    let y = getNum2();
    let result = divide(x, y)
    result_field.value = result
}

function multiplyClick(){
    let x = getNum1();
    let y = getNum2();
    let result = multiply(x, y)
    result_field.value = result
}

function modulusClick(){
    let x = getNum1();
    let y = getNum2();
    let result = modulus(x, y)
    result_field.value = result
}

