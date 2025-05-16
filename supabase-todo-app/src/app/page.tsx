'use client'

import { useEffect, useState } from 'react'
import { supabase } from '@/lib/supabase'
import TodoItem from '@/components/TodoItem'
import { useRouter } from 'next/navigation'

type Todo = {
  id: string
  title: string
  is_done: boolean
}

export default function HomePage() {
  const router = useRouter()
  const [todos, setTodos] = useState<Todo[]>([])
  const [newTodo, setNewTodo] = useState('')
  const [userId, setUserId] = useState<string | null>(null)

  // ユーザー確認とTodo読み込み
  useEffect(() => {
    const fetchUserAndTodos = async () => {
      const {
        data: { session },
      } = await supabase.auth.getSession()

      if (!session?.user) {
        router.push('/auth')
        return
      }

      setUserId(session.user.id)
      await loadTodos(session.user.id)
    }

    fetchUserAndTodos()
  }, [])

  // Todoの読み込み
  const loadTodos = async (uid: string) => {
    const { data, error } = await supabase
      .from('todos')
      .select('*')
      .eq('user_id', uid)
      .order('inserted_at', { ascending: false })

    if (!error && data) {
      setTodos(data)
    }
  }

  // 追加
  const handleAdd = async () => {
    if (!newTodo.trim() || !userId) return

    const { data, error } = await supabase.from('todos').insert({
      title: newTodo,
      user_id: userId,
    })

    if (!error) {
      setNewTodo('')
      await loadTodos(userId)
    }
  }

  // 削除
  const handleDelete = async (id: string) => {
    await supabase.from('todos').delete().eq('id', id)
    if (userId) await loadTodos(userId)
  }

  return (
    <div className="max-w-md mx-auto mt-10 p-4">
      <h1 className="text-2xl font-bold mb-4">Todoリスト</h1>

      <div className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="新しいTodo"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)}
          className="border p-2 flex-1 rounded"
        />
        <button
          onClick={handleAdd}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          追加
        </button>
      </div>

      <div>
        {todos.map((todo) => (
          <TodoItem
            key={todo.id}
            id={todo.id}
            title={todo.title}
            isDone={todo.is_done}
            onDelete={handleDelete}
          />
        ))}
      </div>
    </div>
  )
}
