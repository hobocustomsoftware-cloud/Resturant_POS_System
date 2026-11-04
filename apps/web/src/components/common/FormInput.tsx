interface Props {
  label: string
  value: string
  onChange: (v: string) => void
  type?: string
  error?: string
  required?: boolean
}

export default function FormInput({ label, value, onChange, type = 'text', error, required }: Props) {
  return (
    <div className="mb-4">
      <label className="block mb-1 font-medium">{label}{required && <span className="text-red-600">*</span>}</label>
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className={`w-full border p-2 rounded ${error ? 'border-red-600' : 'border-gray-300'}`}
      />
      {error && <p className="text-red-600 text-sm mt-1">{error}</p>}
    </div>
  )
}
