/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Home' });
});
router.get('/home', function(req, res, next) {
  res.render('index', { title: 'Home' });
});
router.get('/about', function(req, res, next) {
  res.render('about', { title: 'About Me' });
});
router.get('/projects', function(req, res, next) {
  res.render('projects', { title: 'Project' });
});
router.get('/contact', function(req, res, next) {
  res.render('contact', { title: 'Contact Me' });
});
router.get('/services', function(req, res, next) {
  res.render('services', { title: 'Services' });
});

module.exports = router;
