import { resolve } from "url";
import App from '../App'
// import IdxPage from '@/views/index'
const home = resolve => require(['@/views/index'], resolve)
const LoginPage = resolve => require(['@/views/user/login'], resolve)
const TopicPage = resolve => require(['@/views/topic/index'], resolve)
const HeatPage = resolve => require(['@/views/heat/index'], resolve)
const TopicDetailPage = resolve => require(['@/views/topic/topicDetail'], resolve)
const ProfilePage = resolve => require(['@/views/user/profile'], resolve)
const ProfileEditPage = resolve => require(['@/views/user/profileEdit'], resolve)
const QuestionPage = resolve => require(['@/views/question/index'], resolve)
const AllAnswer = resolve => require(['@/views/question/all'], resolve)
const Answer = resolve => require(['@/views/question/answer'], resolve)
const SearchPage = resolve => require(['@/views/search/index'], resolve)
const ErrPage = resolve => require(['@/views/errors/err'], resolve)
export default [{
  path: '/',
  component: App, // 顶级路由, 对应 index.html
  children: [ // 二级路由, 对应 App.vue
    { // 主页
      path: '',
      name: 'home',
      component: home
    },  
    { // 问题详情页
      path: '/question/:q_id',
      component: QuestionPage,
      children: [{
        path: '',
        component: AllAnswer
      },{ // 答案详情页
        path: 'answer/:a_id',
        component: Answer
      }]
    },
    { // 搜索详情页
      path: '/search/',
      component: SearchPage,
      meta: {title: '查找结果'}
    },
    { // 个人信息页
      path: '/profile/:id',
      component: ProfilePage,
    },
    {
      path: '/profile-edit',
      name: 'profileEdit',
      component: ProfileEditPage,
      meta: {title: '修改信息'},
    },
    {
      path: '/topics',
      name: 'topics',
      component: TopicPage,
      meta: {title: '话题'},
    },
    {
      // 话题详情页
      path: '/topic/:id',
      name: 'topic',
      component: TopicDetailPage
    },
    {
      path: '/heat',
      name: 'heat',
      component: HeatPage,
      meta: {title: '热点话题'},
    }
  ]
},
{
  path: '/login',
  name: 'login',
  component: LoginPage,
  meta: {title: '登录注册'},
},
{
  path: "*", 
  name: 'noFound',
  meta: {title: '404 Page Not Found'},
  component: ErrPage,
  data:{
      err:{
        code: 404,
        text: "你似乎来到了没有知识存在的荒原...",
        info: "来源链接是否正确？用户、话题或问题是否存在？"
      }
    }
}]