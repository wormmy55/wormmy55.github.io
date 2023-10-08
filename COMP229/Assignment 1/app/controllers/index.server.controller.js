/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

exports.render = function (req, res) {
    res.render('index', {
        title: 'Hello World'
    })
};
