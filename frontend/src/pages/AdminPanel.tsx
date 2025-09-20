import React, { useState } from 'react'
import { useAuth } from '../hooks/useAuth'
import { useSweets } from '../hooks/useSweets'
import { Sweet, deleteSweet } from '../api/sweetsApi'
import SweetForm from '../components/Admin/SweetForm'

const AdminPanel: React.FC = () => {
  const { isAdmin } = useAuth()
  const { sweets, loading, error, refetch } = useSweets()
  const [showForm, setShowForm] = useState(false)
  const [editingSweet, setEditingSweet] = useState<Sweet | null>(null)

  if (!isAdmin) {
    return <div className="text-center">Access denied. Admin only.</div>
  }

  const handleEdit = (sweet: Sweet) => {
    setEditingSweet(sweet)
    setShowForm(true)
  }

  const handleDelete = async (sweetId: number) => {
    if (window.confirm('Are you sure you want to delete this sweet?')) {
      try {
        await deleteSweet(sweetId)
        refetch()
      } catch (error) {
        console.error('Delete failed:', error)
      }
    }
  }

  const handleFormSuccess = () => {
    setShowForm(false)
    setEditingSweet(null)
    refetch()
  }

  const handleFormCancel = () => {
    setShowForm(false)
    setEditingSweet(null)
  }

  if (showForm) {
    return (
      <SweetForm
        sweet={editingSweet}
        onSuccess={handleFormSuccess}
        onCancel={handleFormCancel}
      />
    )
  }

  return (
    <div>
      <h1>Admin Panel</h1>
      <div className="admin-actions">
        <button 
          onClick={() => setShowForm(true)} 
          className="btn btn-primary"
        >
          Add New Sweet
        </button>
      </div>
      
      {loading && <div className="loading">Loading...</div>}
      {error && <div className="error">Error: {error}</div>}
      
      <div className="grid">
        {sweets.map((sweet) => (
          <div key={sweet.id} className="card sweet-item">
            <h3>{sweet.name}</h3>
            <p className="category">{sweet.category}</p>
            <p className="price">${sweet.price.toFixed(2)}</p>
            <p className={`quantity ${sweet.quantity > 0 ? 'in-stock' : 'out-of-stock'}`}>
              Quantity: {sweet.quantity}
            </p>
            <div className="sweet-actions">
              <button 
                onClick={() => handleEdit(sweet)} 
                className="btn btn-secondary"
              >
                Edit
              </button>
              <button 
                onClick={() => handleDelete(sweet.id)} 
                className="btn btn-danger"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default AdminPanel
