import { useState } from 'react'
import { sendContactMessage } from '../lib/api'
import { Button, Card, SectionHeading } from '../components/ui'

export function ContactPage() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')
  const [status, setStatus] = useState<'idle' | 'sending' | 'sent' | 'error'>('idle')
  const [error, setError] = useState<string | null>(null)

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault()
    setStatus('sending')
    setError(null)
    try {
      await sendContactMessage({ name, email, message })
      setStatus('sent')
      setName('')
      setEmail('')
      setMessage('')
    } catch (e) {
      setStatus('error')
      setError(e instanceof Error ? e.message : 'Failed to send message')
    }
  }

  return (
    <div>
      <SectionHeading
        title="Contact"
        subtitle="Kirim pesan lewat form ini (tersimpan di database via backend)."
      />

      <div className="grid gap-6 lg:grid-cols-2">
        <Card className="p-6">
          <form onSubmit={onSubmit} className="space-y-4">
            <div>
              <label className="text-sm font-medium text-white/80">Nama</label>
              <input
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
                className="mt-2 w-full rounded-xl bg-white/5 px-4 py-2 text-sm text-white ring-1 ring-white/10 placeholder:text-white/40 focus-visible:outline-none"
                placeholder="Nama kamu"
              />
            </div>

            <div>
              <label className="text-sm font-medium text-white/80">Email</label>
              <input
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                type="email"
                className="mt-2 w-full rounded-xl bg-white/5 px-4 py-2 text-sm text-white ring-1 ring-white/10 placeholder:text-white/40 focus-visible:outline-none"
                placeholder="nama@email.com"
              />
            </div>

            <div>
              <label className="text-sm font-medium text-white/80">Pesan</label>
              <textarea
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                required
                rows={6}
                className="mt-2 w-full resize-none rounded-xl bg-white/5 px-4 py-2 text-sm text-white ring-1 ring-white/10 placeholder:text-white/40 focus-visible:outline-none"
                placeholder="Ceritain kebutuhan / peluang kerja / kolaborasi…"
              />
            </div>

            <div className="flex items-center gap-3">
              <Button type="submit" disabled={status === 'sending'}>
                {status === 'sending' ? 'Mengirim…' : 'Kirim'}
              </Button>
              <a className="text-sm font-semibold text-white/70 hover:text-white" href="mailto:you@example.com">
                atau email langsung
              </a>
            </div>

            {status === 'sent' ? (
              <p className="text-sm font-medium text-emerald-300">
                Terkirim. Terima kasih!
              </p>
            ) : null}
            {status === 'error' ? (
              <p className="text-sm font-medium text-rose-300">
                Gagal mengirim. {error ?? ''}
              </p>
            ) : null}
          </form>
        </Card>

        <div className="space-y-4">
          <Card className="p-6">
            <p className="text-sm font-semibold">Info cepat</p>
            <p className="mt-2 text-sm text-white/70">
              - Lokasi: Indonesia
              <br />- Role: Fullstack / Backend
              <br />- Open for: Freelance / Full-time
            </p>
          </Card>
          <Card className="p-6">
            <p className="text-sm font-semibold">Link</p>
            <div className="mt-3 flex flex-col gap-2 text-sm">
              <a className="text-white/70 hover:text-white" href="https://github.com/" target="_blank">
                GitHub
              </a>
              <a className="text-white/70 hover:text-white" href="https://www.linkedin.com/" target="_blank">
                LinkedIn
              </a>
            </div>
          </Card>
        </div>
      </div>
    </div>
  )
}

