/**
 * Created by olenji on 2017/7/1.
 */
var gconfig = require('./config');
var fs = require("fs");
function app_init (){
    //direction create
    mkdir_if_not_found(gconfig.PROCESSED_DIR);
    mkdir_if_not_found(gconfig.UPLOAD_FILE_DIR);

}

function mkdir_if_not_found(dir){
    fs.exists(dir, function(exists) {
        exists? '' : fs.mkdir(dir, function(err){
            if (err)
                console.log(err.message);
            else
                console.log("Create Directory %s", dir);
        });
    });
}
module.exports = app_init;


