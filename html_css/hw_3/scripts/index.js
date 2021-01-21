function hw1(){
	let vernut = ["Число положительное"]
	num1 = document.getElementById('n1').value;

	if (num1 >= 0) {
		vernut = ["Число положительное"]
	}
	else {
		vernut = ["Число Отрицательное"]
	}
	document.getElementById('out').innerHTML = vernut;
}


function hw2(){
	res = 0
	for(i = 0; i < 51; i+=5){
		res += i
	}
	document.getElementById('out2').innerHTML = res;
}

function hw3() {
	var numbers = [254, 115, 78, 25, 91, 45, 37];
	result = []
	for (i in numbers){
		if(numbers[i] > 50){
			result.push(numbers[i])
		}
	}
	document.getElementById('out3').innerHTML = result;
}