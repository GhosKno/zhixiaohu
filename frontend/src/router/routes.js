import { resolve } from "url";

// import IdxPage from '@/views/index'
// import { resolve } from 'dns';
const IdxPage = resolve => require(['@/views/index'], resolve)
const LoginPage = resolve => require(['@/views/user/login'], resolve)
const TopicPage = resolve => require(['@/views/topic/index'], resolve)
export default [{
  path: '/',
  name: 'home',
  component: IdxPage,
}, {
  path: '/login',
  name: 'login',
  component: LoginPage
}, {
  path: '/topic',
  name: 'topic',
  component: TopicPage
}]