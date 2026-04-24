import { useEffect, useMemo, useState } from 'react'
import { listProjects } from '../lib/api'
import type { Project } from '../types'
import { Badge, Button, Card, SectionHeading } from '../components/ui'

export function ProjectsPage() {
  const [projects, setProjects] = useState<Project[] | null>(null)
  const [query, setQuery] = useState('')
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let alive = true
    ;(async () => {
      try {
        const data = await listProjects()
        if (!alive) return
        setProjects(data)
      } catch (e) {
        if (!alive) return
        setError(e instanceof Error ? e.message : 'Failed to load projects')
        setProjects([])
      }
    })()
    return () => {
      alive = false
    }
  }, [])

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase()
    if (!q) return projects ?? []
    return (projects ?? []).filter((p) => {
      return (
        p.name.toLowerCase().includes(q) ||
        p.tagline.toLowerCase().includes(q) ||
        p.description.toLowerCase().includes(q) ||
        p.stack.join(' ').toLowerCase().includes(q)
      )
    })
  }, [projects, query])

  return (
    <div>
      <SectionHeading
        title="Projects"
        subtitle="Daftar project yang bisa kamu tampilkan di portfolio. Kelola datanya dari backend."
      />

      <div className="mb-6 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Cari project (React, API, dsb)"
          className="w-full rounded-xl bg-white/5 px-4 py-2 text-sm text-white ring-1 ring-white/10 placeholder:text-white/40 focus-visible:outline-none sm:max-w-sm"
        />
        <p className="text-sm text-white/60">
          {filtered.length} item{filtered.length === 1 ? '' : 's'}
        </p>
      </div>

      {error ? (
        <Card className="p-5">
          <p className="text-sm font-semibold">Backend belum jalan / error.</p>
          <p className="mt-2 text-sm text-white/70">{error}</p>
          <p className="mt-3 text-sm text-white/70">
            Jalankan backend lalu refresh halaman ini.
          </p>
        </Card>
      ) : null}

      <div className="grid gap-4 sm:grid-cols-2">
        {projects === null
          ? Array.from({ length: 4 }).map((_, idx) => (
              <Card key={idx} className="p-5">
                <div className="h-4 w-2/3 animate-pulse rounded bg-white/10" />
                <div className="mt-3 h-3 w-full animate-pulse rounded bg-white/10" />
                <div className="mt-2 h-3 w-4/5 animate-pulse rounded bg-white/10" />
                <div className="mt-4 flex gap-2">
                  <div className="h-6 w-16 animate-pulse rounded-full bg-white/10" />
                  <div className="h-6 w-20 animate-pulse rounded-full bg-white/10" />
                </div>
              </Card>
            ))
          : filtered.map((p) => (
              <Card key={p.id} className="p-5">
                <div className="flex items-start justify-between gap-3">
                  <div>
                    <h3 className="text-lg font-semibold">{p.name}</h3>
                    <p className="mt-1 text-sm text-white/70">{p.tagline}</p>
                  </div>
                  {p.featured ? <Badge>Featured</Badge> : null}
                </div>
                <p className="mt-3 text-sm text-white/70">{p.description}</p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {p.stack.map((s) => (
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
    </div>
  )
}

