/*
Filename: Assignment 1
Student Name: Jonathan Au
Student ID: 300827701
Date: 09/10/2023
*/

var express = require('express'),
    morgan = require('morgan'),
    compress = require('compression'),
    bodyParser = require('body-parser'),
    methodOverride = require('method-override');

var indexRouter = require('../app/routes/index.server.routes.js');
var homeRouter = require('../app/routes/home.js');
var aboutRouter = require('../app/routes/about.js');
var contactRouter = require('../app/routes/contact.js');
var projectsRouter = require('../app/routes/projects.js');
var servicesRouter = require('../app/routes/services.js');

module.exports = function () {
    var app = express();
    if (process.env.NODE_ENV === 'development') {
        app.use(morgan('dev'));

    } else if (process.env.NODE_ENV === 'production') {
        app.use(compress());
    }

    app.use(bodyParser.urlencoded({
        extended: true
    }));
    app.use(bodyParser.json());
    app.use(methodOverride());
    app.set('views', './app/views');
    app.set('view engine', 'ejs');
    
    app.use('/', indexRouter);
    //require('../app/routes/index.server.routes.js')(app);
    app.use('/home', homeRouter);
    app.use('/about', aboutRouter);
    app.use('/contact', contactRouter);
    app.use('/projects', projectsRouter);
    app.use('/services', servicesRouter);

    app.use(express.static('./public'));
    app.use(express.static("./node_modules"));
    return app;
};
