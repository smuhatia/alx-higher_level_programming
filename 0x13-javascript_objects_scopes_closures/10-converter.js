#!/usr/bin/node

exports.converter = function convertor (base) {
  return x => x.toString(base);
};
