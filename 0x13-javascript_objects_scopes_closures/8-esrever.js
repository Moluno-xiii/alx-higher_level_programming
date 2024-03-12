#!/usr/bin/node
exports.esrever = function (list) {
	const returnedArray = [];

	for (let i = 0; i < list.length; i++) {
		returnedArray.unshift(list[i]);
	}

	return returnedArray;
};
