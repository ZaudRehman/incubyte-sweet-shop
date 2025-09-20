import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

export interface Sweet {
  id: number
  name: string
  category: string
  price: number
  quantity: number
}

export interface CreateSweetData {
  name: string
  category: string
  price: number
  quantity: number
}

const getAuthHeaders = () => {
  const token = localStorage.getItem('token')
  return token ? { Authorization: `Bearer ${token}` } : {}
}

export const getAllSweets = async (): Promise<Sweet[]> => {
  const response = await axios.get(`${API_BASE_URL}/api/sweets`)
  return response.data
}

export const searchSweets = async (query: string): Promise<Sweet[]> => {
  const response = await axios.get(`${API_BASE_URL}/api/sweets/search`, {
    params: { q: query }
  })
  return response.data
}

export const createSweet = async (sweetData: CreateSweetData): Promise<Sweet> => {
  const response = await axios.post(`${API_BASE_URL}/api/sweets`, sweetData, {
    headers: getAuthHeaders()
  })
  return response.data
}

export const updateSweet = async (id: number, sweetData: Partial<CreateSweetData>): Promise<Sweet> => {
  const response = await axios.put(`${API_BASE_URL}/api/sweets/${id}`, sweetData, {
    headers: getAuthHeaders()
  })
  return response.data
}

export const deleteSweet = async (id: number): Promise<void> => {
  await axios.delete(`${API_BASE_URL}/api/sweets/${id}`, {
    headers: getAuthHeaders()
  })
}
