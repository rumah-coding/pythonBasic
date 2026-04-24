import type { PropsWithChildren } from 'react'

export function Card(props: PropsWithChildren<{ className?: string }>) {
  return (
    <div
      className={[
        'rounded-2xl bg-white/5 ring-1 ring-white/10 shadow-[0_10px_30px_rgba(0,0,0,0.25)]',
        props.className ?? '',
      ].join(' ')}
    >
      {props.children}
    </div>
  )
}

export function Badge(props: PropsWithChildren) {
  return (
    <span className="inline-flex items-center rounded-full bg-white/10 px-2.5 py-1 text-xs font-medium text-white/80 ring-1 ring-white/15">
      {props.children}
    </span>
  )
}

export function Button(
  props: PropsWithChildren<{
    href?: string
    onClick?: () => void
    type?: 'button' | 'submit'
    variant?: 'primary' | 'ghost'
    disabled?: boolean
  }>,
) {
  const cls = [
    'inline-flex items-center justify-center rounded-xl px-4 py-2 text-sm font-semibold transition',
    'ring-1 ring-white/15 focus-visible:outline-none',
    props.variant === 'ghost'
      ? 'bg-white/0 text-white/80 hover:bg-white/10 hover:text-white'
      : 'bg-white text-black hover:bg-white/90',
    props.disabled ? 'pointer-events-none opacity-60' : '',
  ].join(' ')

  if (props.href) {
    return (
      <a className={cls} href={props.href} target="_blank" rel="noreferrer">
        {props.children}
      </a>
    )
  }

  return (
    <button
      className={cls}
      type={props.type ?? 'button'}
      onClick={props.onClick}
      disabled={props.disabled}
    >
      {props.children}
    </button>
  )
}

export function SectionHeading(props: { title: string; subtitle?: string }) {
  return (
    <div className="mb-6">
      <h1 className="text-balance text-3xl font-semibold tracking-tight sm:text-4xl">
        {props.title}
      </h1>
      {props.subtitle ? (
        <p className="mt-2 max-w-2xl text-pretty text-white/70">{props.subtitle}</p>
      ) : null}
    </div>
  )
}

