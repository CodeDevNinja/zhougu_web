const tables = [{
  id: '1',
  latitude: 39.915,
  longitude: 116.404,
  date: '2016-05-03',
  name: '王小虎',
  address: '上海市普陀区金沙江路 1518 弄',
  remark: ''
}, {
  id: '1',
  latitude: 39.915,
  longitude: 116.454,
  date: '2016-05-03',
  name: '王小虎',
  address: '上海市普陀区金沙江路 1518 弄',
  remark: ''
}, {
  id: '1',
  latitude: 39.915,
  longitude: 116.444,
  date: '2016-05-03',
  name: '王小虎',
  address: '上海市普陀区金沙江路 1518 弄',
  remark: ''
}]

export default {
  fetchTable: config => {
    // const { username } = JSON.parse(config.body)
    return tables
  }
}
