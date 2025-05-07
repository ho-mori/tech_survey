// app/posts/page.tsx
"use client";

import { useState } from "react";

export default function PostsPage() {
  const [posts, setPosts] = useState<string[]>([]);
  const [input, setInput] = useState("");

  const addPost = () => {
    if (input.trim() !== "") {
      setPosts([...posts, input]);
      setInput("");
    }
  };

  const removePost = (index: number) => {
    setPosts(posts.filter((_, i) => i !== index));
  };

  return (
    <main style={{ padding: 20 }}>
      <h1>Posts</h1>

      <div style={{ marginBottom: 20 }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="New Post"
          style={{ marginRight: 10 }}
        />
        <button onClick={addPost}>Add</button>
      </div>

      <ul>
        {posts.map((post, index) => (
          <li key={index}>
            {post}
            <button
              style={{ marginLeft: 10 }}
              onClick={() => removePost(index)}
            >
              Delete
            </button>
          </li>
        ))}
      </ul>
    </main>
  );
}
