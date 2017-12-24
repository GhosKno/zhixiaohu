// import IdxPage from '@/views/index'
// import { resolve } from 'dns';
const IdxPage = resolve => require(['@/views/index'], resolve)
const LoginPage = resolve => require(['@/views/user/login'], resolve)
export default [{
  path: '/',
  name: 'home',
  component: IdxPage,
}, {
  path: '/login',
  name: 'login',
  component: LoginPage
}]