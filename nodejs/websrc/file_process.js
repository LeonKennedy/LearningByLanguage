var gconfig =  require('./config');
var xlsx = require("node-xlsx");
var fs = require("fs");
var request = require('request');

function Execute(){
    this.entry_audit = function(req, res){
        var filename = req.query.filename;
        var filepath = gconfig.UPLOAD_FILE_DIR + filename;
        fs.stat(filepath, function(err, stats) {
            if (err || !stats.isFile())
                res.end(JSON.stringify({success: false, msg: "File Not Found!"}));
            else
                cai(filepath, res);
        });

    };

    this.summary2entry = function(req, res){
        var filename = req.query.filename;
        var filepath = gconfig.UPLOAD_FILE_DIR + filename;
        fs.stat(filepath, function(err, stats) {
            if (err || !stats.isFile())
                res.end(JSON.stringify({success: false, msg: "File Not Found!"}));
            else
                hua(filepath, res);
        });
    };

    this.freight_audit = function(req, res){
        var filename = req.query.filename;
        var filepath = gconfig.UPLOAD_FILE_DIR + filename;
        fs.stat(filepath, function(err, stats) {
            if (err || !stats.isFile())
                res.end(JSON.stringify({success: false, msg: "File Not Found!"}));
            else
                lion(filepath, res);
        });
    };

}

function hua(filepath, res){
    var filename = filepath.split('/').pop();
    var xlsx_data = xlsx.parse(filepath);
    var sheet = new Array();
    var is_error_format = false;
    xlsx_data[0]['data'].slice(1).forEach(function(item, index){
        if (item.length != 1) is_error_format = true;
        if(item[0])  sheet.push({id: index, summary: item[0]});

    });

    if(is_error_format){
        console.log('returne');
        res.end(JSON.stringify({success:false, msg: 'File Format Fatal'}));
        return;
    }

    function holdbody(body) {
        if (!body) {
            res.end();
            return false;
        }

        var excel_data = new Array();
        excel_data.push(['借', '金额', '贷', '金额', '摘要']);
        body.forEach(function(item){
            excel_data.push([item['debit'], item['debitMoney'], item['credit'] , item['creditMoney'], item['summary']]);
        });

        response_data = {success:true, data:excel_data, filename:filename};
        res.send(JSON.stringify(response_data));
        var buffer = xlsx.build([{data: excel_data, name:'sheet1'}]);
        fs.writeFileSync(gconfig.PROCESSED_DIR + filename, buffer, 'binary');
        res.end();
    }
    var f = req_to_service('http://192.168.1.48:8001/api/accounting_entry/summary2entry', {data:sheet}, holdbody);
    if(f){
        console.log('false request');
        res.end(JSON.stringify({success:false}));
    }
}

function cai(filepath, res){
    var filename = filepath.split('/').pop();
    var xlsx_data = xlsx.parse(filepath);
    var is_bad_format = false;


    var sheet =  new Array();
    xlsx_data[0]['data'].forEach(function(item, index){
        if(typeof item[4]  == 'number' && typeof item[7] == 'number')
            sheet.push({id:index, x: parseFloat(item[4]), y: parseFloat(item[7])});
        else
            if(index != 0 && !item) is_bad_format = true;

    });


    //verify excel format
    if (is_bad_format){
        res.end(JSON.stringify({success:false, msg: 'File Format Fatal'}));
        return;
    }

    function holdbody(body){
        if (!body) return false;
        xlsx_data[0]['data'].forEach(function(item, index){
            item.push(1);
            body.forEach(function(itemE, indexE){
                if( index == parseInt( itemE['id'])){
                    item.pop();
                    item.push(itemE['c']);
                    item[1] = 0;
                }
            });
        });

        response_data = {success:true, data:xlsx_data[0]['data'], filename:filename};
        res.send(JSON.stringify(response_data));
        var buffer = xlsx.build(xlsx_data);
        fs.writeFileSync(gconfig.PROCESSED_DIR + filename, buffer, 'binary');
        res.end();
    }
    var errdata = req_to_service('http://192.168.1.48:8000/api/entry_audit', sheet, holdbody);
    //write to file
}

function lion(filepath, res) {
    var filename = filepath.split('/').pop();
    var xlsx_data = xlsx.parse(filepath);
    var is_bad_format = false;

    var sheet =  new Array();
    xlsx_data[0]['data'].forEach(function(item, index){
        if(typeof item[2]  == 'number' && typeof item[3] == 'number' && typeof item[4] == 'number' && typeof item[5] == 'number')
            sheet.push({id:index, a: parseFloat(item[2]), b:parseFloat(item[3]), c: parseFloat(item[4]), d: parseFloat(item[5])});
        else
            if(index != 0 && !item) is_bad_format = true;

    });

    if (is_bad_format){

        res.end(JSON.stringify({success:false, msg: 'File Format Fatal'}));
        return;
    }

    function holdbody(body){
        if (!body) return false;
        xlsx_data[0]['data'].forEach(function(item, index){
            if (index !=0){
                item[6] = 1;
                item[1] = 1;
            }
            body.forEach(function(itemE, indexE){
                if( index == parseInt( itemE['id'])){
                    item[6] = itemE['c'];
                    item[1] = 0;
                }
            });
        });

        response_data = {success:true, data:xlsx_data[0]['data'], filename:filename};
        res.end(JSON.stringify(response_data));
        var buffer = xlsx.build(xlsx_data);
        fs.writeFileSync(gconfig.PROCESSED_DIR + filename, buffer, 'binary');

    }

    req_to_service('http://192.168.1.48:8000/api/freight_audit', sheet, holdbody);

}

function req_to_service(url, params, holdbody){
    console.log("request to service : %s", url);
    var options = { method: 'POST',
        url: url,
        headers:
            {   'cache-control': 'no-cache',
                'content-type': 'application/json'
            },
        body: params,
        json: true };

    request(options, function (error, response, body) {
        if (error) throw new Error(error);
        if ( response.statusCode == 200 ){
            holdbody(body['data']);
        }else{
            console.log('status code : %d', response.statusCode);
            console.log(body);
            }
    });
}

module.exports = Execute;
