import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className='flex-col my-10 mx-auto w-1/2 align-center'>
        <h1 className="text-3xl font-bold underline">
          Hello world!
        </h1>
        <button onClick={() => setCount((count) => count + 1)} className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded'>
          count is {count}
        </button>
      </div>
    </>
  )
}

export default App
