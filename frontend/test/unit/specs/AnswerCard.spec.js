import Vue from 'vue'
import AnswerCard from '@/components/AnswerCard'

const DATA = {
  answer: {
    'id': 1,
    'userSummary': {
      'id': 2,
      'avatar': 'http://127.0.0.1:8000/media/avatar/L2psOURyaytOSXZUTzFrbXRWL0dvb1lrUXlMNXpvb3MvODlpYnZPMHNSSG1FQ0JXOWdoYW1BPT0_xy3e0D6.jpg',
      'nickname': '马丽亚',
      'description': ''
    },
    'approve': 3,
    'question': {
      'id': 4,
      'title': '地球的半径是多少？'
    },
    'has_approve': false,
    'has_against': false,
    'has_favorite': false,
    'add_time': '2018-01-11T07:32:28.321107Z',
    'detail': '<p>ddd</p>',
    'comment_count': 5
  },
  showQuestion: false
}

describe('AnswerCard.vue', () => {
  it('answer 为空', () => {
    const Constructor = Vue.extend(AnswerCard)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.info')).to.not.exist
    expect(vm.copyText).to.equal('')
  })
  it('answer 不为空, showQuestion 为false', () => {
    const Constructor = Vue.extend(AnswerCard)
    const vm = new Constructor(DATA).$mount()
    setTimeout(_ => {
      expect(vm.$el.querySelector('.info')).to.be.exist
      expect(vm.$el.querySelector('.question')).to.not.exist
      expect(vm.$data.copyText).to.equal('地球的半径是多少？ 马丽亚的回答 - 知小乎 http://' +
        window.location.host + '/question/4/answer/1')
      done()
    }, 200)
  })
  it('点击用户昵称', () => {
    const Constructor = Vue.extend(AnswerCard)
    const vm = new Constructor(DATA).$mount()
    const name = vm.$el.querySelector('.name')
    name.click()
    vm.$nextTick(() => {
      expect(vm.$route.path).to.equal('/profile/2')
      done()
    })
  })
})
