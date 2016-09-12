/**
 * Just a proof of concept, usign the same algorithm as in the python version
 * but now written in javascript for benchmark purposes
 */
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('data.csv')
});

var days = {
	'0': 0,
	'1': 0,
	'2': 0,
	'3': 0,
	'4': 0,
	'5': 0,
	'6': 0,
	'7': 0,
};

lineReader.on('line', (line) => {
	var pieces = line.split(',');
	day = pieces[3];
	days[pieces[3]] += 1
});

lineReader.on('close', () =>  {
	var max  = 0;
	var maxkey = '';
	for (var key in days) {
		if (days[key] > max) {
			max = days[key];
			maxkey = key;
		}
	}
	console.log(`El día con más tráfico es el ${maxkey} con ${max} coches en suma`);
});
