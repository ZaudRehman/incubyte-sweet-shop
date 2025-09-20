import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

export interface LoginCredentials {
  email: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
}

export interface AuthResponse {
  access_token: string
  token_type: string
  user: {
    id: number
    username: string
    email: string
    is_admin: boolean
  }
}

export const login = async (credentials: LoginCredentials): Promise<AuthResponse> => {
  const response = await axios.post(`${API_BASE_URL}/api/auth/login`, credentials)
  return response.data
}

export const register = async (userData: RegisterData): Promise<AuthResponse> => {
  const response = await axios.post(`${API_BASE_URL}/api/auth/register`, userData)
  return response.data
}
