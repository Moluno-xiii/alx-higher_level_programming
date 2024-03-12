#!/usr/bin/node

let numOfTimes = -1;

exports.logMe = function (item) {
	numOfTimes += 1;
	console.log(`${numOfTimes} : ${item}`)
};
