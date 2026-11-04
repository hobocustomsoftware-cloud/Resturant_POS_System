import { View, Text, TouchableOpacity } from 'react-native'
import { router } from 'expo-router'

export default function Home() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 20 }}>Restaurant POS</Text>
      <TouchableOpacity onPress={() => router.push('/pos')} style={{ backgroundColor: '#2563eb', padding: 12, borderRadius: 8, marginBottom: 10, width: '100%' }}>
        <Text style={{ color: 'white', textAlign: 'center' }}>POS</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => router.push('/kds')} style={{ backgroundColor: '#16a34a', padding: 12, borderRadius: 8, marginBottom: 10, width: '100%' }}>
        <Text style={{ color: 'white', textAlign: 'center' }}>KDS</Text>
      </TouchableOpacity>
      <TouchableOpacity onPress={() => router.push('/tables')} style={{ backgroundColor: '#ea580c', padding: 12, borderRadius: 8, width: '100%' }}>
        <Text style={{ color: 'white', textAlign: 'center' }}>Tables</Text>
      </TouchableOpacity>
    </View>
  )
}
