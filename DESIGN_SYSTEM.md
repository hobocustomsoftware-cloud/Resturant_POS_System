# Restaurant POS - Modern Clean Design System

## Design Philosophy
- **Minimal & Clean**: Focus on functionality, reduce visual clutter
- **Modern UI**: Card-based layouts, subtle shadows, rounded corners
- **Intuitive**: Easy to use for non-technical staff
- **Responsive**: Works on desktop, tablet, mobile
- **Consistent**: Unified design language across all platforms

## Color Palette
```css
/* Primary */
--primary-50: #eff6ff
--primary-500: #3b82f6
--primary-600: #2563eb
--primary-700: #1d4ed8

/* Success */
--success-500: #10b981
--success-600: #059669

/* Warning */
--warning-500: #f59e0b
--warning-600: #d97706

/* Danger */
--danger-500: #ef4444
--danger-600: #dc2626

/* Neutral */
--gray-50: #f9fafb
--gray-100: #f3f4f6
--gray-200: #e5e7eb
--gray-300: #d1d5db
--gray-600: #4b5563
--gray-900: #111827
```

## Typography
- **Font Family**: Inter, system-ui, -apple-system, sans-serif
- **Headings**: 24px, 20px, 18px, 16px (bold/semibold)
- **Body**: 14px, 16px
- **Small**: 12px, 13px

## Spacing
- Base unit: 4px
- Scale: 4, 8, 12, 16, 24, 32, 48, 64px

## Components

### Button
```tsx
<button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors">
  Primary Button
</button>
```

### Card
```tsx
<div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
  Card Content
</div>
```

### Input
```tsx
<input className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" />
```

## Layout Patterns

### POS Layout
```
┌─────────────────────────────────────────────────────────┐
│ Header: Logo | Order Type | Tables | KDS | Admin       │
├─────────────┬─────────────────────────┬─────────────────┤
│ Categories   │ Menu Items Grid         │ Cart Panel      │
│ (Sidebar)    │ (Product Cards)         │ (Order Summary) │
└─────────────┴─────────────────────────┴─────────────────┘
```

### Admin Layout
```
┌─────────┬─────────────────────────────────────────────────┐
│ Sidebar │ Header | Content Area                            │
│ (Nav)   │ (Breadcrumbs) | Data Table / Forms              │
└─────────┴─────────────────────────────────────────────────┘
```

## UI Improvements Needed
1. **POS**: Cleaner card design, better spacing, smooth animations
2. **Admin**: Modern sidebar, data tables with sorting/filtering
3. **Forms**: Consistent input styling, better validation states
4. **Modals**: Clean overlays with proper focus management
5. **Loading States**: Skeleton loaders
6. **Empty States**: Helpful illustrations/messages

## Implementation Plan
- Update Tailwind config with extended colors/shadows
- Create reusable component library
- Refactor POS UI to cleaner design
- Refactor Admin UI to modern layout
- Add animations and transitions
- Ensure mobile responsiveness
