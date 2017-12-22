// import IdxPage from '@/views/index'
// import { resolve } from 'dns';
const IdxPage = resolve => require(['@/views/index'], resolve)
export default [{
  path: '/',
  name: 'home',
  component: IdxPage,
}]