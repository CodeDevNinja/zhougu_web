<template>
  <div>
    <el-table
      ref="multipleTable"
      :key="tableKey"
      :data="tableData"
      border
      fit
      highlight-current-row
      tooltip-effect="dark"
      style="width: 100%"
      @selection-change="handleSelectionChange">
      <el-table-column
        type="selection"
        width="55"/>
      <el-table-column
        label="设备编号"
        width="120">
        <template slot-scope="scope">{{ scope.row.id }}</template>
      </el-table-column>
      <el-table-column
        prop="name"
        label="设备名称"
        width="120"/>
      <el-table-column
        prop="longitude"
        label="经度"
        show-overflow-tooltip/>
      <el-table-column
        prop="latitude"
        label="纬度"
        show-overflow-tooltip/>
      <el-table-column
        prop="address"
        label="地址"
        show-overflow-tooltip/>
      <el-table-column
        prop="remark"
        label="备注"
        show-overflow-tooltip/>
      <el-table-column label="操作" align="center" width="230" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">修改</el-button>
          <!--<el-button v-if="scope.row.status!='published'" size="mini" type="success" @click="handleModifyStatus(scope.row,'published')">{{ $t('table.publish') }}-->
          <!--</el-button>-->
          <!--<el-button size="mini" @click="handleModifyStatus(scope.row,'draft')">{{ $t('table.draft') }}-->
          <!--</el-button>-->
          <el-button size="mini" type="danger" @click="handleDelete(scope.row)">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div style="margin-top: 20px;align: right">
      <!--<el-button @click="toggleSelection([tableData[1], tableData[2]])">切换第二、第三行的选中状态</el-button>-->
      <el-button
        style="align: right"
        @click="toggleSelection()">选中删除
      </el-button>
      <el-button
        style="align: right"
        @click="open_add_device_dialog()">添加设备
      </el-button>
    </div>
    <!--地图-->
    <bmap :point_datas="tableData" style="margin-top: 10px"/>
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="70px"
               style="width: 400px; margin-left:50px;">
        <el-form-item label="设备编号" prop="id">
          <el-input v-model="temp.id"/>
        </el-form-item>
        <el-form-item label="设备名称">
          <el-input v-model="temp.name"/>
        </el-form-item>
        <el-form-item label="经度">
          <el-input v-model="temp.longitude"/>
        </el-form-item>
        <el-form-item label="纬度">
          <el-input v-model="temp.latitude"/>
        </el-form-item>
        <el-form-item label="备注">
          <el-input v-model="temp.remark"/>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button v-if="dialogStatus=='create'" type="primary" @click="add_device_data">添加</el-button>
        <el-button v-else type="primary" @click="updateData">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import {fetchTable} from '@/api/deviceTable'
  import bmap from '@/views/map/index'

  export default {
    components: {bmap},
    data() {
      return {
        tableKey: '',
        temp: {
          id: undefined,
          latitude: '',
          longitude: '',
          date: '',
          name: '',
          address: '',
          remark: ''
        },
        dialogFormVisible: false,
        dialogStatus: '',
        textMap: {
          update: '修改设备',
          create: '添加设备'
        },
        tableData: [{
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
        }],
        multipleSelection: []
      }
    },
    created() {
      this.init_data()
    },
    methods: {
      init_data() {
        fetchTable().then(response => {
          // this.tableData = response
          console.log('=========')
          console.log(response.data)
        })
      },
      open_add_device_dialog(rows) {
        this.dialogFormVisible = true
        this.dialogStatus = 'create'
        this.temp = ''
      },
      add_device_data() {
        console.log('++++++++++++++')
        console.log(this.$refs['dataForm'])
        console.log(this.temp.name)
        console.log(this.temp)
        const tempData = Object.assign({}, this.temp)
        console.log(tempData)
        this.tableData.push(tempData)
        this.dialogFormVisible = false
        console.log(this.tableData)
      },
      toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            console.log(this.$refs.multipleTable)
            this.handleDelete(row)
            this.$refs.multipleTable.toggleRowSelection(row)
          })
        } else {
          this.$refs.multipleTable.clearSelection()
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val
      },
      handleUpdate(row) {
        this.temp = Object.assign({}, row) // copy obj
        this.dialogFormVisible = true
        this.dialogStatus = 'update'
      },
      updateData() {
        for (const v of this.tableData) {
          if (v.id === this.temp.id) {
            const index = this.tableData.indexOf(v)
            this.tableData.splice(index, 1, this.temp)
            break
          }
        }
        this.dialogFormVisible = false
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
      },
      handleDelete(row) {
        // 删除数据
        const index = this.tableData.indexOf(row)
        this.tableData.splice(index, 1)
      }
    }
  }
</script>
