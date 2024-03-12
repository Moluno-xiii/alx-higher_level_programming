#!/usr/bin/node

let numOfTimes = 0;

exports.logMe = function (item) {
	console.log(`${numOfTimes} : ${item}`);
	numOfTimes++;
};
