var xlsx = require('node-xlsx');
var fs = require('fs');
var filepath = '';
var outfilepath = '';

// read excel to js object
var xlsx_data = xlsx.parse(filepath);
console.log(xlsx_data);

// save object to file
var buffer = xlsx.build(xlsx_data);
fs.writeFileSync(outfilepath, buffer, 'binary');



