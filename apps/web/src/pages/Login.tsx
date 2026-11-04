export default function Login() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h1 className="text-2xl font-bold mb-6">Login</h1>
        <input className="w-full border p-2 mb-4 rounded" placeholder="Username" />
        <input className="w-full border p-2 mb-4 rounded" type="password" placeholder="Password" />
        <button className="w-full bg-blue-600 text-white p-2 rounded">Login</button>
      </div>
    </div>
  )
}
