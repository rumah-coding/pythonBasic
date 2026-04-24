export type Project = {
  id: number
  name: string
  tagline: string
  description: string
  stack: string[]
  links: { label: string; url: string }[]
  featured: boolean
  created_at: string
}

export type BlogPost = {
  id: number
  title: string
  slug: string
  summary: string
  content_md: string
  tags: string[]
  published_at: string
}

export type ContactMessageInput = {
  name: string
  email: string
  message: string
}

