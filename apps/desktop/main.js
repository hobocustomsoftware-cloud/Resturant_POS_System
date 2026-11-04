const { app, BrowserWindow, Menu } = require('electron')
const path = require('path')

function createWindow() {
  const win = new BrowserWindow({
    width: 1400,
    height: 900,
    minWidth: 1024,
    minHeight: 768,
    title: 'Restaurant POS',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  })
  Menu.setApplicationMenu(null)
  win.loadURL(process.env.POS_URL || 'http://localhost:5173/pos')
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow()
})
