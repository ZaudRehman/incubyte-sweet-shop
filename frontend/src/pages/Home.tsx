import React from 'react'
import { useSweets } from '../hooks/useSweets'
import SweetList from '../components/Dashboard/SweetList'
import SearchBar from '../components/common/SearchBar'

const Home: React.FC = () => {
  const { sweets, loading, error, refetch, searchSweets } = useSweets()

  const handleSearch = (query: string) => {
    if (query.trim()) {
      searchSweets(query)
    } else {
      refetch()
    }
  }

  return (
    <div>
      <h1 className="text-center mb-1">Sweet Shop</h1>
      <SearchBar onSearch={handleSearch} />
      <SweetList 
        sweets={sweets} 
        loading={loading} 
        error={error} 
        onUpdate={refetch} 
      />
    </div>
  )
}

export default Home
