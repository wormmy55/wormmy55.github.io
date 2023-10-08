/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

var express = require('express');
var router = express.Router();

router.get('/contact', function(req, res, next) {
    res.render('contact', { title: 'Contact Me' });
});

module.exports = router;
