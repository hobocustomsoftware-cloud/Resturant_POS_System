import React from 'react'
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native'

export default function HomeScreen({ navigation }: any) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Restaurant POS</Text>
      <TouchableOpacity style={styles.btn} onPress={() => navigation.navigate('POS')}>
        <Text style={styles.btnText}>POS</Text>
      </TouchableOpacity>
      <TouchableOpacity style={[styles.btn, {backgroundColor:'#16a34a'}]} onPress={() => navigation.navigate('KDS')}>
        <Text style={styles.btnText}>Kitchen Display</Text>
      </TouchableOpacity>
      <TouchableOpacity style={[styles.btn, {backgroundColor:'#ea580c'}]} onPress={() => navigation.navigate('Tables')}>
        <Text style={styles.btnText}>Tables</Text>
      </TouchableOpacity>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', padding: 20, backgroundColor: '#f9fafb' },
  title: { fontSize: 28, fontWeight: 'bold', textAlign: 'center', marginBottom: 40 },
  btn: { backgroundColor: '#2563eb', padding: 16, borderRadius: 8, marginBottom: 12 },
  btnText: { color: 'white', textAlign: 'center', fontSize: 16, fontWeight: '600' }
})
