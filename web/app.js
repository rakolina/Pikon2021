'use strict';

const http = require('http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

const getHtml = () => {
  try {
    return fs.readFileSync('pikon.html', 'utf8');
  } catch (err) {
    console.error(err);
  } finally {
    console.log('html loading is done');
  }
};

const getParams = (buffer) => {
  const params = {};
  buffer.split('&').forEach((p) => {
    const keyValue = p.split('=');
    const key = keyValue[0].replace(/\+/g, ' ');
    const value = keyValue[1];
    params[key] = value ;
  });
  return params;
};

const saveConfig = (buffer) => {
  const params = getParams(buffer);
  const config = {
    image_format: params.encoding,
    iso: params.iso,
    shutter_speed: params['shutter speed seconds'],
  };
  console.log(`New config: ${JSON.stringify(config)}`);
  fs.writeFile('pikon.conf', JSON.stringify(config), (err) => {
    err ? console.error(err) : console.log('Configuration file saved');
  });
  return config;
};

const homePage = (req, res) => {
  res.writeHeader(200, {'Content-Type': 'text/html'});
  res.end(getHtml());
};

const save = (req, res) => {
  let buffer = '';
  req.on('data', chunk => { buffer += chunk; });
  req.on('end', () => {
    const config = saveConfig(buffer);
    console.log(`Responding with: ${JSON.stringify(config)}`);
    res.writeHead(200, 'Content-Type: text/plain');
    res.end(`New config: ${JSON.stringify(config)}`);
  });
};

const server = http.createServer((req, res) => {
  console.log(req.url);
  switch (req.url) {
    case '/':
      homePage(req, res);
      break;
    case '/save':
      save(req, res);
      break;
    default:
      homePage(req, res);
  };
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

