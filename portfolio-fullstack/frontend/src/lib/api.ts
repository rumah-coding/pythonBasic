import type { BlogPost, ContactMessageInput, Project } from '../types'

const API_BASE =
  import.meta.env.VITE_API_BASE?.toString() || 'http://127.0.0.1:8000'

async function http<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    ...init,
    headers: {
      'content-type': 'application/json',
      ...(init?.headers ?? {}),
    },
  })
  if (!res.ok) {
    const text = await res.text().catch(() => '')
    throw new Error(text || `Request failed (${res.status})`)
  }
  return (await res.json()) as T
}

export async function listProjects(): Promise<Project[]> {
  return await http<Project[]>('/api/projects')
}

export async function listPosts(): Promise<BlogPost[]> {
  return await http<BlogPost[]>('/api/posts')
}

export async function sendContactMessage(input: ContactMessageInput): Promise<void> {
  await http<void>('/api/contact', {
    method: 'POST',
    body: JSON.stringify(input),
  })
}

