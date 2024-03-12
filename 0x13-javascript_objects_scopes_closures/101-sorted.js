#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const val = Object.values(dict);
const valUniq = [...new Set(val)];
const newDict = {};
for (const j in valUniq) {
  const list = [];
  for (const k in totalist) {
    if (totalist[k][1] === valUniq[j]) {
      list.unshift(totalist[k][0]);
    }
  }
  newDict[valUniq[j]] = list;
}
console.log(newDict);
