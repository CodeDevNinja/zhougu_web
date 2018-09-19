<template>
  <div id="allmap" :style="{height:mapHeight+'px'}"/>
  <!--<h3>{{ point_datas }}</h3>-->
</template>

<script>
  import BMap from 'BMap'

  export default {
    name: 'Dashboard',
    props: {
      point_datas: {
        type: Array,
        default: null
      }
    },
    data() {
      return {
        mapHeight: 100
        // points: [
        //   [
        //     116.417854,
        //     39.921988,
        //
        //     '设备：XXXX<br>电话：13800138000<br>时间：2018-03-16 18：00：05<br>位置：北京市东城区正义路甲5号'
        //   ],
        //   [
        //     116.412222,
        //     30.912345,
        //     '设备：XXXX<br>电话：13800138000<br>时间：2018-03-16 18：00：05<br>位置：北京市东城区正义路甲5号'
        //   ]
        // ]
      }
    },
    computed: {},
    mounted() {
      console.log(this.point_datas)
      // 百度地图API功能
      const map = new BMap.Map('allmap', {enableMapClick: false})
      map.centerAndZoom(new BMap.Point(116.417854, 39.921988), 12)
      map.enableScrollWheelZoom()

      var geolocation = new BMap.Geolocation()
      geolocation.enableSDKLocation()
      geolocation.getCurrentPosition(function (r) {
        if (this.getStatus() === 0) {
          map.panTo(r.point)
        }
      }, {enableHighAccuracy: true})

      this.mapHeight =
        (window.innerHeight ||
          document.documentElement.clientHeight ||
          document.body.clientHeight) - 85
      this.point_datas.forEach(function (element) {
        var marker = new BMap.Marker(
          new BMap.Point(element.longitude, element.latitude)
        )
        // 创建标注
        var content = '名称：' + element.name + '<br>经度:' + element.longitude + '<br>纬度:' + element.latitude + '<br>位置：' + element.address
        map.addOverlay(marker) // 将标注添加到地图中
        addClickHandler(content, marker)
        console.log(element)
      })
      var opts = {
        width: 250, // 信息窗口宽度
        // height: 80,     // 信息窗口高度
        title: '设备信息', // 信息窗口标题
        enableMessage: false // 设置不允许信息窗发送短息
      }

      function addClickHandler(content, marker) {
        marker.addEventListener('click', function (e) {
          openInfo(content, e)
        })
      }

      function openInfo(content, e) {
        var p = e.target
        var point = new BMap.Point(p.getPosition().lng, p.getPosition().lat)
        var infoWindow = new BMap.InfoWindow(content, opts) // 创建信息窗口对象
        map.openInfoWindow(infoWindow, point) // 开启信息窗口
      }

      // fetchCarsGps().then(res => {
      // var marker = new BMap.Marker(
      //   new BMap.Point(116.406605, 39.921585)
      // )
      // // 创建标注
      // var content = '设备：XXXX<br>电话：13800138000<br>时间：2018-03-16 18：00：05<br>位置：北京市东城区正义路甲5号\'\n'
      // map.addOverlay(marker) // 将标注添加到地图中
      // addClickHandler(content, marker)
      // });
    },
    methods: {}
  }
</script>

<style rel="stylesheet/scss" lang="scss">
  #allmap {
    width: 100%;
    height: 100%;

    p {
      margin-left: 5px;
      font-size: 14px;
    }
  }

  .anchorBL {
    display: none;
  }
</style>
