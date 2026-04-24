import { Link } from 'react-router-dom'
import { Button, Card, SectionHeading } from '../components/ui'

export function NotFoundPage() {
  return (
    <div>
      <SectionHeading title="Not found" subtitle="Halaman yang kamu cari tidak ada." />
      <Card className="p-6">
        <p className="text-sm text-white/70">Coba kembali ke halaman utama.</p>
        <div className="mt-4">
          <Link to="/">
            <Button>Ke Home</Button>
          </Link>
        </div>
      </Card>
    </div>
  )
}

