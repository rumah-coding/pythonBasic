import { Outlet } from 'react-router-dom'
import { Footer } from './Footer'
import { Navbar } from './Navbar'

export function Layout() {
  return (
    <div className="min-h-dvh">
      <Navbar />
      <main className="mx-auto w-full max-w-6xl px-4 pb-16 pt-10 sm:px-6">
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}

