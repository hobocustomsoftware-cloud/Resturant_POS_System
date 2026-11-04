export const validateEmail = (email: string) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
export const validateRequired = (value: any) => value !== '' && value !== null && value !== undefined
