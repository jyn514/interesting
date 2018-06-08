#!/usr/bin/env node
console.log('hello and welcome to the javascript house of horrors');
console.log("we'll show you a little of what we have here today:");
require('./utils').readFile(__filename);

for (obj of [Array(5), Array(5).keys(), Array.from(Array(5).keys())]) {
	console.log(obj);
}
console.log('wait, what?')

for (obj in Array(5).keys()) {
	console.log(obj);
}

for (obj of Array(5).keys()) {
	console.log(obj);
}

console.log("wait, **what?!?**");
