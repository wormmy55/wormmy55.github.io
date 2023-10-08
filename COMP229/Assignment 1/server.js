/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

process.env.NODE_ENV = process.env.NODE_ENV || 'development';
var express = require('./config/express');
var app = express();
app.listen(5000);
module.exports = app;

console.log('Server running at http://localhost:5000/');
