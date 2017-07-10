// basic setup
var express = require('express');
var app = express();

// express middlewares
app.use(express.static("./public")); // setup static directory

// app init
var app_init= require('./initialization');
app_init();

// load modules
var UserManager = require('./user_manager'); // TODO remove this sample module later
user_manager = new UserManager();

var FileManager = require('./file_manager');
file_manager = new FileManager();

var Execute = require('./file_process');
execute = new Execute();

var port = process.env.PORT || 8089; // TODO move into config file

// setup routers
var router = express.Router(); // 获得express router对象

// router middlewares 
// any requests will go through all the router middlewares in sequence, 
// and be processed by handler if matched

// allow CORS, that is cross-origin HTTP request (TODO disable CORS in production?)
router.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
    res.header("X-Powered-By",' 3.2.1'); 
    res.header("Content-Type", "application/json;charset=utf-8");
    next(); // pass on to next middleware, or matched handler if no middleware is available
});

// log for each request
router.use(function (req, res, next) {
    console.log('method: ' + req.method + ', url: ' + req.url);
    next();
});

// all the routers go here

router.get('/user', function (req, res) { // TODO remove this sample router later
    user_manager.get_user(req, res);
});

router.post('/file', function (req, res) {
    file_manager.upload(req, res);     
});

router.get('/entry_audit', function(req, res){
    execute.entry_audit(req, res);
});

router.get('/summary2entry', function(req, res){
    execute.summary2entry(req, res);
});

router.get('/freight_audit', function(req, res){
    execute.freight_audit(req, res);
});




// register router with prefix '/api'
app.use('/api', router);

// start server and listen
app.listen(port);
console.log('API server is running on port: ' + port);
