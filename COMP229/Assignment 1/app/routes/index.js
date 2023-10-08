/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

var express = require('express');
var router = express.Router();
/*
router.get('/', function(req, res, next) {
    res.render('index', { title: 'Home' });
  });*/
router.get('/home', function(req, res, next) {
    res.render('index', { title: 'Home' });
});
 
module.exports = router;
