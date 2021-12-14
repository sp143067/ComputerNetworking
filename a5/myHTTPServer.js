// declaring required modules to establish an HTTP server
var http = require('http');
var fs   = require('fs');

// Host & Port declaration
var HOST = process.argv.slice(2,3);
var PORT = Number(process.argv.slice(3,4));

// calling the 'createServer' class to deploy the HTTP server
http.createServer(function(req, res) {
    if (req.url == '/index.html' || req.url == '/') {
        fs.readFile('./index.html', function(err, data) {
            res.end(data);
        });
    } else if (req.url == '/time') {
        //let t2 = new Date().getTime();
        let t2 = Date.now();
        // console.log("printing time t2")
        // added code to decode message and display them on the server console,
            // this way I'm adding a delay between t2 and t3 to see some RTT difference.
        let msg = 'Sending t2 & t3 time in JSON format!';
        let myBuff = new Buffer(msg);
        let decodedMsg = myBuff.toString('base64');
        console.log(msg);

        let t3 = Date.now();
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({ 't2': t2, 't3': t3}));
    } else {
        fs.readFile('./my404.html', function(err, data) {
                res.end(data);
            });
    }
}).listen(PORT, HOST);
console.log("HTTP Server is running on '" + HOST + "' with port " + PORT + ".....");