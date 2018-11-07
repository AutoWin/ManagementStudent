var fs=require('fs');
var data=fs.readFileSync('test.json', 'utf8');
var words=JSON.parse(data);
console.log(words);
