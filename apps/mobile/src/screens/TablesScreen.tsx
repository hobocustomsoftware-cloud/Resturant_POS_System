import React from 'react'
import { View, Text, StyleSheet } from 'react-native'

export default function TablesScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Tables</Text>
      <Text>Table layout</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, backgroundColor: '#f9fafb' },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 16 }
})
