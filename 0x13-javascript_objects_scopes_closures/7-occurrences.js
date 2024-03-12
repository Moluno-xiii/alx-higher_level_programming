#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	const occurence = 0;
	for (let i = 0; i < list.length; i++) {
		list[i] === searchElement && occurence++
	}

	return occurence;
};
