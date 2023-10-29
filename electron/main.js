const {app, BrowserWindow } = require('electron');
const {PythonShell} = require('python-shell');


app.whenReady().then(() => {

    let pyshell = new PythonShell('..//python/speechrec.py');

    pyshell.on('message', function(message) {
        console.log(message);
      })

    const myWindow = new BrowserWindow({
        autoHideMenuBar: true,
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    

    // load a webpage
    myWindow.loadFile("index.html");
})