import Vue from 'vue'
import AnswerCard from '@/components/AnswerCard'

describe('AnswerCard.vue', () => {
  it('answer 为空', () => {
    const Constructor = Vue.extend(AnswerCard)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.info')).to.not.exist
    expect(vm.$data.copyText).to.equal('')
  })
  it('answer 不为空', () => {
    const Constructor = Vue.extend(AnswerCard)
    const vm = new Constructor({
      answer: {
        'id': 5,
        'userSummary': {
          'id': 1,
          'avatar': 'http://127.0.0.1:8000/media/avatar/L2psOURyaytOSXZUTzFrbXRWL0dvb1lrUXlMNXpvb3MvODlpYnZPMHNSSG1FQ0JXOWdoYW1BPT0_xy3e0D6.jpg',
          'nickname': '马丽亚',
          'description': ''
        },
        'approve': 4,
        'question': {
          'id': 1,
          'title': '地球的半径是多少？'
        },
        'has_approve': false,
        'has_against': false,
        'has_favorite': false,
        'add_time': '2018-01-11T07:32:28.321107Z',
        'detail': '<p>ddd</p>',
        'comment_count': 15
      }
    }).$mount()
    var info = vm.$el.querySelector('.info')
    expect(info).to.exist()
    expect(vm.$data.copyText).to.equal('地球的半径是多少？ 马丽亚的回答 - 知小乎 http://' + 
    window.location.host + '/question/1/answer/5')
  })
})
