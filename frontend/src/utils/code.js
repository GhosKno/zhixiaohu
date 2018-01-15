const encodeHex = (str) => {
  const temp = new Buffer(str)
  return temp.toString('hex')
}

const decodeHex = (str) => {
  const temp = new Buffer(str, 'hex')
  return temp.toString('utf8')
}

const encodeBase64 = (str) => {
  const temp = new Buffer(str)
  return temp.toString('base64')
}

const decodeBase64 = (str) => {
  const temp = new Buffer(str, 'base64')
  return temp.toString()
}

const multiEncode = (str) => {
  return encodeHex(encodeBase64(str))
}

const multiDecode = (str) => {
  return decodeBase64(decodeHex(str))
}

module.exports = {
  encodeHex,
  decodeHex,
  encodeBase64,
  decodeBase64,
  multiEncode,
  multiDecode
}