import request from '@/utils/request'

export function fetchTable(query) {
  return request({
    url: '/',
    method: 'get',
    params: query
  })
}
