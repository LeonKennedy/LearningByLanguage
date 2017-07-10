var request = require('request');

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
        return 0;
    }else{
        console.log('status code : %d', response.statusCode);
        console.log(body);
        return 1;
    }
});
