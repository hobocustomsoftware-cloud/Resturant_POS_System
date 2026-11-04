const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld('electronAPI', {
  newOrder: () => ipcRenderer.send('new-order'),
  onNewOrder: (callback) => ipcRenderer.on('new-order', callback)
})
