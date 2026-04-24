export function Footer() {
  return (
    <footer className="border-t border-white/10">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-2 px-4 py-10 text-sm text-white/60 sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <p>© {new Date().getFullYear()} Yoyo. Built with React + FastAPI.</p>
        <div className="flex gap-4">
          <a className="hover:text-white" href="https://github.com/" target="_blank">
            GitHub
          </a>
          <a className="hover:text-white" href="https://www.linkedin.com/" target="_blank">
            LinkedIn
          </a>
          <a className="hover:text-white" href="mailto:you@example.com">
            Email
          </a>
        </div>
      </div>
    </footer>
  )
}

