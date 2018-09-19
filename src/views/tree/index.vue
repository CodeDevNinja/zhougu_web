<template>
  <div class="app-container">
    <el-input v-model="filterText" placeholder="Filter keyword" style="margin-bottom:30px;"/>

    <el-tree
      ref="tree2"
      :data="data2"
      :props="defaultProps"
      :filter-node-method="filterNode"
      class="filter-tree"
      default-expand-all
    />

  </div>
</template>

<script>
  export default {
    data() {
      return {
        filterText: '',
        data2: [{
          id: 1,
          label: '增加设备'
        },
          {
            id: 1,
            label: '删除设备'
          },
          {
            id: 1,
            label: '修改设备'
          },
          {
            id: 1,
            label: '设备1',
            children: [
              {
                id: 4,
                label: '在线控制与状态数据显示'
              },
              {
                id: 9,
                label: '位置信息电子地图'
              }, {
                id: 10,
                label: '设备图像视频'
              }
            ]
          },
          {
            id: 2,
            label: '设备2',
            children: [{
              id: 5,
              label: '在线控制与状态数据显示'
            }, {
              id: 6,
              label: '位置信息电子地图'
            },
              {
                id: 10,
                label: '设备图像视频'
              }]

          }]
      }
    },
    defaultProps: {
      children: 'children',
      label: 'label'
    },
    watch: {
      filterText(val) {
        this.$refs.tree2.filter(val)
      }
    },

    methods: {
      filterNode(value, data) {
        if (!value) return true
        return data.label.indexOf(value) !== -1
      }
    }
  }
</script>

