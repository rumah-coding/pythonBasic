import { useEffect, useMemo, useState } from 'react'
import { Link } from 'react-router-dom'
import { listProjects } from '../lib/api'
import type { Project } from '../types'
import { Badge, Button, Card, SectionHeading } from '../components/ui'

const fallbackProjects: Project[] = [
  {
    id: 1,
    name: 'Portfolio Fullstack',
    tagline: 'React + FastAPI + SQLite',
    description:
      'Template portfolio yang profesional: Projects, Blog, Contact form, dan API backend.',
    stack: ['React', 'Tailwind', 'FastAPI', 'SQLite'],
    links: [{ label: 'Source', url: 'https://github.com/' }],
    featured: true,
    created_at: new Date().toISOString(),
  },
]

export function HomePage() {
  const [projects, setProjects] = useState<Project[] | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    let alive = true
    ;(async () => {
      try {
        const data = await listProjects()
        if (alive) setProjects(data)
      } catch {
        if (alive) setProjects(fallbackProjects)
      }
      if (alive) setLoading(false)
    })()
    return () => {
      alive = false
    }
  }, [])

  const featured = useMemo(
    () => (projects ?? []).filter((p) => p.featured).slice(0, 3),
    [projects],
  )

  return (
    <div className="space-y-10">
      <section className="relative overflow-hidden rounded-3xl bg-white/5 p-8 ring-1 ring-white/10 sm:p-12">
        <div className="absolute inset-0 bg-[radial-gradient(600px_250px_at_20%_20%,rgba(255,255,255,0.12),transparent_60%)]" />
        <div className="relative">
          <p className="text-sm font-medium text-white/70">Fullstack Developer</p>
          <h1 className="mt-3 text-balance text-4xl font-semibold tracking-tight sm:text-5xl">
            Bangun produk yang cepat, rapi, dan enak dipakai.
          </h1>
          <p className="mt-4 max-w-2xl text-pretty text-white/70">
            Portfolio ini siap kamu kustom: tampil profesional, ada data proyek & blog dari
            backend, plus contact form yang masuk ke database.
          </p>

          <div className="mt-6 flex flex-wrap gap-3">
            <Button href="https://github.com/">GitHub</Button>
            <Link to="/projects">
              <Button variant="ghost">Lihat Projects</Button>
            </Link>
            <Link to="/contact">
              <Button variant="ghost">Kontak</Button>
            </Link>
          </div>

          <div className="mt-8 flex flex-wrap gap-2">
            <Badge>React</Badge>
            <Badge>Tailwind</Badge>
            <Badge>FastAPI</Badge>
            <Badge>SQLite</Badge>
            <Badge>REST API</Badge>
          </div>
        </div>
      </section>

      <section>
        <SectionHeading
          title="Featured Projects"
          subtitle="Beberapa project pilihan. Data diambil dari backend (atau fallback jika backend belum jalan)."
        />

        {loading ? (
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {Array.from({ length: 3 }).map((_, i) => (
              <Card key={i} className="p-5">
                <div className="h-4 w-2/3 animate-pulse rounded bg-white/10" />
                <div className="mt-3 h-3 w-full animate-pulse rounded bg-white/10" />
                <div className="mt-2 h-3 w-4/5 animate-pulse rounded bg-white/10" />
              </Card>
            ))}
          </div>
        ) : (
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {featured.map((p) => (
              <Card key={p.id} className="p-5">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <h3 className="text-lg font-semibold">{p.name}</h3>
                    <p className="mt-1 text-sm text-white/70">{p.tagline}</p>
                  </div>
                  <Badge>Featured</Badge>
                </div>
                <p className="mt-3 text-sm text-white/70">{p.description}</p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {p.stack.slice(0, 5).map((s) => (
                    <Badge key={s}>{s}</Badge>
                  ))}
                </div>
                <div className="mt-5 flex flex-wrap gap-2">
                  {p.links.map((l) => (
                    <Button key={l.url} href={l.url} variant="ghost">
                      {l.label}
                    </Button>
                  ))}
                </div>
              </Card>
            ))}
          </div>
        )}

        <div className="mt-6">
          <Link to="/projects" className="text-sm font-semibold text-white/80 hover:text-white">
            Lihat semua project →
          </Link>
        </div>
      </section>
    </div>
  )
}

