import { useState, useEffect } from 'react'
import { Sweet, getAllSweets, searchSweets } from '../api/sweetsApi'

export const useSweets = () => {
  const [sweets, setSweets] = useState<Sweet[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  const fetchSweets = async () => {
    try {
      setLoading(true)
      setError(null)
      const data = await getAllSweets()
      setSweets(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch sweets')
    } finally {
      setLoading(false)
    }
  }

  const searchSweetsData = async (query: string) => {
    try {
      setLoading(true)
      setError(null)
      const data = await searchSweets(query)
      setSweets(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to search sweets')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchSweets()
  }, [])

  return {
    sweets,
    loading,
    error,
    refetch: fetchSweets,
    searchSweets: searchSweetsData
  }
}
