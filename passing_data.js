var one;
var two;
var add;
function a(){
  one = 1;
  two = 2;
}
function b(){
  var array = []
  var add = one + two; 
  array.push(one)
  array.push(two)
  array.push(add)
  console.log(array)
}

a()
b()
