import React from 'react'

export default class ErrorBoundary extends React.Component<any, any> {
  constructor(props: any) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError() {
    return { hasError: true }
  }

  render() {
    if (this.state.hasError) {
      return <div className="p-6 text-center">Something went wrong.</div>
    }
    return this.props.children
  }
}
