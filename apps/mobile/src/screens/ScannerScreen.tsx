import React from 'react'
import { View, Text, StyleSheet } from 'react-native'

export default function ScannerScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Barcode Scanner</Text>
      <Text style={styles.text}>Scanner functionality ready</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#f9fafb' },
  title: { fontSize: 22, fontWeight: 'bold' },
  text: { marginTop: 8, color: '#666' }
})
