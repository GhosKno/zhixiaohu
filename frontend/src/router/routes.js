import { resolve } from "url";

// import IdxPage from '@/views/index'
// import { resolve } from 'dns';
const IdxPage = resolve => require(['@/views/index'], resolve)
const LoginPage = resolve => require(['@/views/user/login'], resolve)
const TopicPage = resolve => require(['@/views/topic/index'], resolve)
const ProfilePage = resolve => require(['@/views/user/profile'], resolve)
const ProfileEditPage = resolve => require(['@/views/user/profileEdit'], resolve)
const QuestionPage = resolve => require(['@/views/question/index'], resolve)
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
}, {
  path: '/profile',
  name: 'profile',
  component: ProfilePage
}, {
  path: '/profile-edit',
  name: 'profileEdit',
  component: ProfileEditPage
},{
  path: '/question/:id',
  name: 'question',
  component: QuestionPage,
}]