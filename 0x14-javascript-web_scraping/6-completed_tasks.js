#!/usr/bin/node

const retrieve = require('request');

retrieve.get(process.argv[2], (error, res, body) => {
  if (error) console.log(error);
  else {
    const computed = {};
    const todos = JSON.parse(body);
    todos.forEach(task => {
      if (task.completed) {
        if (!computed[task.userId]) computed[task.userId] = 1;
        else computed[task.userId] += 1;
      }
    });
    console.log(computed);
  }
});
