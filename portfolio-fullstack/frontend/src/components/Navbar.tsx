import { NavLink } from 'react-router-dom'

const nav = [
  { to: '/', label: 'Home' },
  { to: '/projects', label: 'Projects' },
  { to: '/blog', label: 'Blog' },
  { to: '/contact', label: 'Contact' },
] as const

export function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-white/10 bg-black/10 backdrop-blur supports-[backdrop-filter]:bg-black/5">
      <div className="mx-auto flex w-full max-w-6xl items-center justify-between px-4 py-3 sm:px-6">
        <NavLink
          to="/"
          className="group inline-flex items-center gap-2 rounded-xl px-2 py-1 font-semibold tracking-tight"
        >
          <span className="inline-flex h-8 w-8 items-center justify-center rounded-xl bg-white/10 ring-1 ring-white/15 transition group-hover:bg-white/15">
            Y
          </span>
          <span>Yoyo</span>
        </NavLink>

        <nav className="flex items-center gap-1">
          {nav.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={({ isActive }) =>
                [
                  'rounded-xl px-3 py-2 text-sm font-medium transition',
                  'text-white/70 hover:text-white hover:bg-white/10',
                  isActive ? 'bg-white/10 text-white ring-1 ring-white/15' : '',
                ].join(' ')
              }
              end={item.to === '/'}
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </div>
    </header>
  )
}

