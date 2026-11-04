import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'
import HomeScreen from './src/screens/HomeScreen'
import POSScreen from './src/screens/POSScreen'
import KDSScreen from './src/screens/KDSScreen'
import TablesScreen from './src/screens/TablesScreen'

const Stack = createNativeStackNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="POS" component={POSScreen} />
        <Stack.Screen name="KDS" component={KDSScreen} />
        <Stack.Screen name="Tables" component={TablesScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}
