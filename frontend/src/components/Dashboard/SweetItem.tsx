import React, { useState } from 'react'
import { Sweet } from '../../api/sweetsApi'
import { purchaseSweet } from '../../api/inventoryApi'
import { useAuth } from '../../hooks/useAuth'
import '../../styles/components.css'

interface SweetItemProps {
  sweet: Sweet
  onUpdate: () => void
}

const SweetItem: React.FC<SweetItemProps> = ({ sweet, onUpdate }) => {
  const [loading, setLoading] = useState(false)
  const { user } = useAuth()

  const handlePurchase = async () => {
    if (!user || sweet.quantity === 0) return
    
    setLoading(true)
    try {
      await purchaseSweet(sweet.id)
      onUpdate()
    } catch (error) {
      console.error('Purchase failed:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="card sweet-item">
      <h3>{sweet.name}</h3>
      <p className="category">{sweet.category}</p>
      <p className="price">${sweet.price.toFixed(2)}</p>
      <p className={`quantity ${sweet.quantity > 0 ? 'in-stock' : 'out-of-stock'}`}>
        {sweet.quantity > 0 ? `In Stock: ${sweet.quantity}` : 'Out of Stock'}
      </p>
      {user && (
        <button
          onClick={handlePurchase}
          disabled={sweet.quantity === 0 || loading}
          className="btn btn-primary"
        >
          {loading ? 'Purchasing...' : 'Purchase'}
        </button>
      )}
    </div>
  )
}

export default SweetItem
