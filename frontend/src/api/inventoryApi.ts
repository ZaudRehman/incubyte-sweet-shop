import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

const getAuthHeaders = () => {
  const token = localStorage.getItem('token')
  return token ? { Authorization: `Bearer ${token}` } : {}
}

export const purchaseSweet = async (sweetId: number): Promise<void> => {
  await axios.post(`${API_BASE_URL}/api/sweets/${sweetId}/purchase`, {}, {
    headers: getAuthHeaders()
  })
}

export const restockSweet = async (sweetId: number, quantity: number): Promise<void> => {
  await axios.post(`${API_BASE_URL}/api/sweets/${sweetId}/restock`, { quantity }, {
    headers: getAuthHeaders()
  })
}
