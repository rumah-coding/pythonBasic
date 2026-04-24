import { useEffect, useState } from 'react'
import { listPosts } from '../lib/api'
import type { BlogPost } from '../types'
import { Badge, Card, SectionHeading } from '../components/ui'

export function BlogPage() {
  const [posts, setPosts] = useState<BlogPost[] | null>(null)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    let alive = true
    ;(async () => {
      try {
        const data = await listPosts()
        if (!alive) return
        setPosts(data)
      } catch (e) {
        if (!alive) return
        setError(e instanceof Error ? e.message : 'Failed to load posts')
        setPosts([])
      }
    })()
    return () => {
      alive = false
    }
  }, [])

  return (
    <div>
      <SectionHeading
        title="Blog"
        subtitle="Tulisan singkat tentang apa yang kamu pelajari / bangun. Konten diambil dari backend."
      />

      {error ? (
        <Card className="p-5">
          <p className="text-sm font-semibold">Backend belum jalan / error.</p>
          <p className="mt-2 text-sm text-white/70">{error}</p>
        </Card>
      ) : null}

      <div className="grid gap-4">
        {(posts ?? Array.from({ length: 3 })).map((p, idx) =>
          typeof p === 'object' ? (
            <Card key={p.id} className="p-5">
              <div className="flex flex-wrap items-baseline justify-between gap-3">
                <h3 className="text-lg font-semibold">{p.title}</h3>
                <p className="text-xs text-white/50">
                  {new Date(p.published_at).toLocaleDateString()}
                </p>
              </div>
              <p className="mt-2 text-sm text-white/70">{p.summary}</p>
              <div className="mt-4 flex flex-wrap gap-2">
                {p.tags.map((t) => (
                  <Badge key={t}>{t}</Badge>
                ))}
              </div>
            </Card>
          ) : (
            <Card key={idx} className="p-5">
              <div className="h-4 w-2/3 animate-pulse rounded bg-white/10" />
              <div className="mt-3 h-3 w-full animate-pulse rounded bg-white/10" />
              <div className="mt-2 h-3 w-4/5 animate-pulse rounded bg-white/10" />
              <div className="mt-4 flex gap-2">
                <div className="h-6 w-14 animate-pulse rounded-full bg-white/10" />
                <div className="h-6 w-16 animate-pulse rounded-full bg-white/10" />
              </div>
            </Card>
          ),
        )}

        {posts && posts.length === 0 && !error ? (
          <Card className="p-5">
            <p className="text-sm text-white/70">
              Belum ada post. Tambahkan dari backend seed/admin.
            </p>
          </Card>
        ) : null}
      </div>
    </div>
  )
}

