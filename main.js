const { app, BrowserWindow } = require('electron')
const path = require('path');
var IMG_DIR = '/img/';

function createWindow () {
  // Create the browser window.
  win = new BrowserWindow({
    width: 800,
    height: 600,
    icon: path.join(__dirname +'\\logo1.png'),
    frame: false,
  });

  // and load the index.html of the app.
  //win.openDevTools({detach: true});
  //win.loadFile('index.html')
  win.loadURL('http://localhost:5000/base');
  win.on("closed", () => {
  win = null;
  });
};

app.on('ready', createWindow);