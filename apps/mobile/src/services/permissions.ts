import { Platform } from 'react-native'

export const requestCameraPermission = async () => {
  if (Platform.OS === 'web') return true
  return true
}
