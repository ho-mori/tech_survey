'use client'
import { useState } from 'react'

type Props = {
  id: string
  title: string
  isDone: boolean
  onDelete: (id: string) => void
}

export default function TodoItem({ id, title, isDone, onDelete }: Props) {
  return (
    <div className="flex justify-between items-center border p-2 my-2">
      <span className={isDone ? 'line-through' : ''}>{title}</span>
      <button className="text-red-500" onClick={() => onDelete(id)}>
        削除
      </button>
    </div>
  )
}
