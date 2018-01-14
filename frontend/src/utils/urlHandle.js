const transUrl = (url) => {
  if (url.includes('127.0.0.1') || url.includes('http')) {
    let re = /(\w+):\/\/([^\:|\/]+)(\:\d*)?(.*\/)([^#|\?|\n]+)?(#.*)?(\?.*)?/i;
    return url.match(re).slice(4).join('')
  }
  return url
}

export default {
  install(Vue, options) {
    Vue.prototype.transUrl = transUrl
  }
}