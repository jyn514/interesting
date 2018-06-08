#!/usr/bin/env node

const fs = require('fs');
exports.readFile = function (filename) {
	console.log("'''");
	process.stdout.write(fs.readFileSync(filename).toString('utf8'));
	console.log("'''");
}
