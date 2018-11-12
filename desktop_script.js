var fs=require('fs');
var data=fs.readFileSync('test.json', 'utf8');
var words=JSON.parse(data);
console.log(words);
console.log(words.length);
console.log(words[0].MSV);
console.log(words[0].idle1.TC);
