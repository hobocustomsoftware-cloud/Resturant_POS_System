import React from 'react'
import { View, Text, StyleSheet } from 'react-native'

export default function KDSScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Kitchen Display</Text>
      <Text>Orders</Text>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 16, backgroundColor: '#111827' },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 16, color: 'white' }
})
