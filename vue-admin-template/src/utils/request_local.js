import axios from 'axios'

const baseURL =
  process.env.NODE_ENV === 'development'
    ? // ? 'https://sls-mockserver.staging.shopeemobile.com/atp'
    'http://127.0.0.1:8001/atp'
    : // ? 'http://127.0.0.1:8000/atp'
    location.origin + '/atp'

const request_local = axios.create({
  baseURL,
  timeout: 5000,
  headers: { 'content-type': 'application/json' }
})

export default request_local
