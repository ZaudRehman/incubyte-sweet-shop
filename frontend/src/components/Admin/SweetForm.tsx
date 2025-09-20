import React, { useState, useEffect } from 'react'
import { Sweet, CreateSweetData, createSweet, updateSweet } from '../../api/sweetsApi'

interface SweetFormProps {
  sweet?: Sweet | null
  onSuccess: () => void
  onCancel: () => void
}

const SweetForm: React.FC<SweetFormProps> = ({ sweet, onSuccess, onCancel }) => {
  const [formData, setFormData] = useState<CreateSweetData>({
    name: '',
    category: '',
    price: 0,
    quantity: 0
  })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (sweet) {
      setFormData({
        name: sweet.name,
        category: sweet.category,
        price: sweet.price,
        quantity: sweet.quantity
      })
    }
  }, [sweet])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError('')

    try {
      if (sweet) {
        await updateSweet(sweet.id, formData)
      } else {
        await createSweet(formData)
      }
      onSuccess()
    } catch (err) {
      setError('Operation failed. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: name === 'price' || name === 'quantity' ? Number(value) : value
    }))
  }

  return (
    <div className="form-container">
      <h2>{sweet ? 'Update Sweet' : 'Add New Sweet'}</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="category">Category</label>
          <input
            type="text"
            id="category"
            name="category"
            value={formData.category}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="price">Price</label>
          <input
            type="number"
            id="price"
            name="price"
            value={formData.price}
            onChange={handleChange}
            min="0"
            step="0.01"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="quantity">Quantity</label>
          <input
            type="number"
            id="quantity"
            name="quantity"
            value={formData.quantity}
            onChange={handleChange}
            min="0"
            required
          />
        </div>
        {error && <div className="error-message">{error}</div>}
        <div className="sweet-actions">
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? 'Saving...' : (sweet ? 'Update' : 'Add')}
          </button>
          <button type="button" onClick={onCancel} className="btn btn-secondary">
            Cancel
          </button>
        </div>
      </form>
    </div>
  )
}

export default SweetForm
