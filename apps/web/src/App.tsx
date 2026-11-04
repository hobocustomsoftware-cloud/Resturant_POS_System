import { Routes, Route, Navigate } from 'react-router-dom'
import POS from './pages/POS'
import KDS from './pages/KDS'
import Admin from './pages/Admin'
import DailyOpening from './pages/DailyOpening'
import DailyPurchases from './pages/DailyPurchases'
import DailyClose from './pages/DailyClose'
import ReportsDaily from './pages/ReportsDaily'
import ReportsMonthly from './pages/ReportsMonthly'
import Login from './pages/Login'

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/pos" element={<POS />} />
      <Route path="/kds" element={<KDS />} />
      <Route path="/admin/*" element={<Admin />} />
      <Route path="/daily/opening" element={<DailyOpening />} />
      <Route path="/daily/purchases" element={<DailyPurchases />} />
      <Route path="/daily/close" element={<DailyClose />} />
      <Route path="/reports/daily" element={<ReportsDaily />} />
      <Route path="/reports/monthly" element={<ReportsMonthly />} />
      <Route path="/tables" element={<Tables />} />
      <Route path="/" element={<Navigate to="/pos" replace />} />
    </Routes>
  )
}

export default App

import Tables from './pages/Tables'
