import { Navigate, Route, Routes } from 'react-router-dom'
import { Layout } from './components/Layout'
import { BlogPage } from './pages/Blog'
import { ContactPage } from './pages/Contact'
import { HomePage } from './pages/Home'
import { ProjectsPage } from './pages/Projects'
import { NotFoundPage } from './pages/NotFound'

function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<HomePage />} />
        <Route path="/projects" element={<ProjectsPage />} />
        <Route path="/blog" element={<BlogPage />} />
        <Route path="/contact" element={<ContactPage />} />
        <Route path="/home" element={<Navigate to="/" replace />} />
        <Route path="*" element={<NotFoundPage />} />
      </Route>
    </Routes>
  )
}

export default App
