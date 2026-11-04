import React from 'react'
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native'
import { useCartStore } from '../store/cartStore'

export default function PaymentScreen({ navigation }: any) {
  const { total, clear } = useCartStore()
  const cartTotal = total()

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Payment</Text>
      <View style={styles.card}>
        <Text style={styles.total}>Total: {cartTotal} MMK</Text>
        <TouchableOpacity style={styles.btn} onPress={() => { clear(); navigation.navigate('Home') }}>
          <Text style={styles.btnText}>Complete Payment (Cash)</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.btn, {backgroundColor:'#4f46e5'}]}>
          <Text style={styles.btnText}>Card</Text>
        </TouchableOpacity>
        <TouchableOpacity style={[styles.btn, {backgroundColor:'#06b6d4'}]}>
          <Text style={styles.btnText}>QR</Text>
        </TouchableOpacity>
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f9fafb', padding: 16 },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 20 },
  card: { backgroundColor: '#fff', padding: 20, borderRadius: 8 },
  total: { fontSize: 20, fontWeight: 'bold', marginBottom: 20, textAlign: 'center' },
  btn: { backgroundColor: '#16a34a', padding: 14, borderRadius: 6, marginBottom: 10 },
  btnText: { color: '#fff', textAlign: 'center', fontWeight: '600' }
})
