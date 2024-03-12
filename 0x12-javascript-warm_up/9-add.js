#!/usr/bin/node

const firstNumber = Number(process.argv[2]);
const secondNumber = Number(process.argv[3]);

function addNumbers (firstNumber, secondNumber) {
	return(firstNumber + secondNumber);
}

console.log(addNumbers(firstNumber, secondNumber));
