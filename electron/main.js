const {app, BrowserWindow } = require('electron')

app.whenReady().then(() => {

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