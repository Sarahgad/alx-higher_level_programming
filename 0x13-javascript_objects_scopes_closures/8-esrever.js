#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    array[j] = list[i];
    j++;
  }
  return array;
};
