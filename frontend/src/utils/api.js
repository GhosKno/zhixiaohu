import Vue from 'vue'

const USER = '/api/users/'
const PROFILE = '/api/profiles/';
const QUESTION = '/api/questions/';
const TOPIC = '/api/topics/';
const ANSWER = '/api/answers/';
const COMMENT = '/api/comments/';
const MESSAGE = '/api/messages/';
const MEDIA = '/api/media/';

export default {
  login(data) {
    return Vue.http.post(USER + 'login/', data)
  },
  logout() {
    return Vue.http.get(USER + 'logout/')
  },
  register(data) {
    return Vue.http.post(USER + 'register/', data)
  },
  resetPwd(data) {
    return Vue.http.post(USER + 'rest_password/', data)
  },
  getMessages() {
    return Vue.http.get(USER + 'messages/')
  },
  watchSb(id) {
    return Vue.http.get(USER + id + '/watch/')
  },
  cancelWatchSb(id) {
    return Vue.http.get(USER + id + '/cancel_watch/')
  },

  uploadAvatar(data) {
    return Vue.http.post(PROFILE + 'avatar/', data)
  },
  updateInfo(data) {
    return Vue.http.post(PROFILE + 'update_info/', data)
  },
  getProfile(id) {
    return Vue.http.get(PROFILE + id)
  },
  getActiveties(id) {
    return Vue.http.get(PROFILE + id + '/activities/')
  },
  getWatchQuestion(id) {
    return Vue.http.get(PROFILE + id + '/watched_questions/')
  },
  getHerQuestion(id) {
    return Vue.http.get(PROFILE + id + '/questions/')
  },
  getHerAnswers(id) {
    return Vue.http.get(PROFILE + id + '/answers/')
  },
  getFollower(id) {
    return Vue.http.get(PROFILE + id + '/be_watched/')
  },
  getFocusOn(id) {
    return Vue.http.get(PROFILE + id + '/watched_users/')
  },
  getStar(id) {
    return Vue.http.get(PROFILE + id + '/favorites/')
  },
  getHistory(id) {
    return Vue.http.get(PROFILE + id + '/history/')
  },
  postQuestion(data) {
    return Vue.http.post(QUESTION, data)
  },
  getQuestions() {
    return Vue.http.get(QUESTION)
  },
  getQuestion(id) {
    return Vue.http.get(QUESTION + id)
  },
  watchQuestion(id) {
    return Vue.http.get(QUESTION + id + '/watch/')
  },
  cancelWatchQuestion(id) {
    return Vue.http.get(QUESTION + id + '/cancel_watch/')
  },
  getAnswersByQuestion(id) {
    return Vue.http.get(QUESTION + id + '/get_answers/')
  },

  searchQuestion(str, page = 0) {
    return Vue.http.get('/api/questions?' + (page ? 'page=' + page + '&' : '') + 'search=' + str)
  },
  searchTopics(str, page = 0) {
    return Vue.http.get('/api/topics?' + (page ? 'page=' + page + '&' : '') + 'search=' + str)
  },
  searchAnswers(str, page = 0) {
    return Vue.http.get('/api/answers?' + (page ? 'page=' + page + '&' : '') + 'search=' + str)
  },
  searchProfile(str, page = 0) {
    return Vue.http.get('/api/profiles?' + (page ? 'page=' + page + '&' : '') + 'search=' + str)
  },

  getAllTopics() {
    return Vue.http.get(TOPIC)
  },
  getTopic(id) {
    return Vue.http.get(TOPIC + id)
  },
  createTopic(data) {
    return Vue.http.post(TOPIC, data)
  },
  getHotTopics() {
    return Vue.http.get(TOPIC + 'hot/')
  },
  getQuestionsByTopic(id) {
    return Vue.http.get(TOPIC + id + '/get_questions/')
  },
  getAnswersByTopic(id) {
    return Vue.http.get(TOPIC + id + '/get_answers/')
  },


  postAnswer(data) {
    return Vue.http.post(ANSWER, data)
  },
  updateAnswer(id, data) {
    return Vue.http.put(ANSWER + id + '/', data)
  },
  getAnswers() {
    return Vue.http.get(ANSWER)
  },
  getAnswer(id) {
    return Vue.http.get(ANSWER + id)
  },
  zanAnswer(id) {
    return Vue.http.get(ANSWER + id + '/agree/')
  },
  cancelZanAnswer(id) {
    return Vue.http.get(ANSWER + id + '/cancel_agree/')
  },
  caiAnswer(id) {
    return Vue.http.get(ANSWER + id + '/disagree/')
  },
  CancelCaiAnswer(id) {
    return Vue.http.get(ANSWER + id + '/cancel_disagree/')
  },
  starAnswer(id) {
    return Vue.http.get(ANSWER + id + '/favorite/')
  },
  CancelStarAnswer(id) {
    return Vue.http.get(ANSWER + id + '/cancel_favorite/')
  },
  getComments(id, page) {
    return Vue.http.get(ANSWER + id + '/get_comments' + (page ? '?page=' + page : '/'))
  },
  postComment(data) {
    return Vue.http.post(COMMENT, data)
  },
  markRead(id) {
    return Vue.http.get(MESSAGE + id + '/readed/')
  },
  getUnreadNum(id) {
    return Vue.http.get(MESSAGE + 'unread/')
  }
}