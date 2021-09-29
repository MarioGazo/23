const express = require('express');
const app = express();
const fs = require('fs');
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

// Get all users
app.get('/assets', function(req, res){
    fs.readFile("./assets.json", 'utf8', function(err, data){
        // Return all users
        res.end(data);
    });
})

// Get a user
app.get('/assets/:id', function(req, res){
    fs.readFile("./assets.json", 'utf8', function(err, data){
        const jsonData = JSON.parse(data);
        if (!jsonData[req.params.id]) {
            res.end("User doesn't exist");
            return;
        }

        // Return user
        res.end(JSON.stringify(jsonData[req.params.id], null, 2));
    });
})

// Delete a user
app.delete('/assets/:id', function(req, res){
    fs.readFile('./assets.json', 'utf8', function(err, data){
        const jsonData = JSON.parse(data);
        if (!jsonData[req.params.id]) {
            res.end("User doesn't exist");
            return;
        }
        delete jsonData[req.params.id];
        fs.writeFile('./assets.json', JSON.stringify(jsonData, null, 2), function (err,data) {
            if (err) {
                return console.log(err);
            }
        });
    });
});

// Update a user
app.put('/assets/:id', function(req, res){
    fs.readFile('./assets.json', 'utf8', function(err, data){
        const jsonData = JSON.parse(data);
        if (!jsonData[req.params.id]) {
            res.end("User doesn't exist");
            return;
        }

        if (req.body.title) jsonData[req.params.id]['title'] = req.body.title;
        if (req.body.label) jsonData[req.params.id]['label'] = req.body.label;
        if (req.body.url) jsonData[req.params.id]['label'] = req.body.url;

        fs.writeFile('./assets.json', JSON.stringify(jsonData, null, 2), function (err,data) {
            if (err) {
                return console.log(err);
            }
        });
        res.end(JSON.stringify(jsonData[req.params.id], null, 2));
    });
});

// Returns first free asset ID
function getFreeId(array) {
    let i = 1;
    while (array[i]) { i++; }
    return i;
}

// Create a user
app.post('/assets', function(req, res){
    fs.readFile("./assets.json", 'utf8', function(err, data){
        const newUser = req.body;
        const jsonData = JSON.parse(data);
        const newId = getFreeId(jsonData);
        jsonData[newId] = newUser;
        fs.writeFile('./assets.json', JSON.stringify(jsonData, null, 2), function (err,data) {
            if (err) {
                return console.log(err);
            }
        });
        res.end(JSON.stringify(newUser, null, 2));
    });
})

module.exports = app;
