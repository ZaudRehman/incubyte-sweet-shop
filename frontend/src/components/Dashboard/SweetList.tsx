import React from 'react'
import { Sweet } from '../../api/sweetsApi'
import SweetItem from './SweetItem'

interface SweetListProps {
  sweets: Sweet[]
  loading: boolean
  error: string | null
  onUpdate: () => void
}

const SweetList: React.FC<SweetListProps> = ({ sweets, loading, error, onUpdate }) => {
  if (loading) {
    return <div className="loading">Loading sweets...</div>
  }

  if (error) {
    return <div className="error">Error: {error}</div>
  }

  if (sweets.length === 0) {
    return <div className="text-center">No sweets found.</div>
  }

  return (
    <div className="grid">
      {sweets.map((sweet) => (
        <SweetItem key={sweet.id} sweet={sweet} onUpdate={onUpdate} />
      ))}
    </div>
  )
}

export default SweetList
