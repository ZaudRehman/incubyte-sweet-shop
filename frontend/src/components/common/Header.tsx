import React from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../../hooks/useAuth'
import '../../styles/components.css'

const Header: React.FC = () => {
  const { user, logout, isAdmin } = useAuth()

  return (
    <header className="header">
      <div className="header-content">
        <Link to="/" className="logo">
          🍭 Sweet Shop
        </Link>
        <nav>
          <ul className="nav-links">
            <li><Link to="/">Home</Link></li>
            {user ? (
              <>
                {isAdmin && <li><Link to="/admin">Admin</Link></li>}
                <li>
                  <span>Hello, {user.username}</span>
                </li>
                <li>
                  <button onClick={logout} className="btn btn-secondary">
                    Logout
                  </button>
                </li>
              </>
            ) : (
              <>
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/register">Register</Link></li>
              </>
            )}
          </ul>
        </nav>
      </div>
    </header>
  )
}

export default Header
