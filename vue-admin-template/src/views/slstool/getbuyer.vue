<template>
  <div class="app-container">

    <el-row type="justify"
            justify="space-between">
      <el-col push=1>
        <el-form :inline="true"
                 :model="formsearch"
                 :rules="rules"
                 class="demo-form-inline">
          <el-form-item label="环境">
            <el-select id="select"
                       v-model="formsearch.env"
                       @change="getBuyer('')"
                       filterable
                       clearable
                       placeholder="请选择">
              <el-option v-for="item in env_opt"
                         :key="item.value"
                         :label="item.label"
                         :value="item.value">{{item.value}}</el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="国家">
            <el-select v-model="formsearch.country"
                       @change="getBuyer('')"
                       filterable
                       clearable
                       placeholder="请选择">
              <el-option v-for="item in country_opt"
                         :key="item.value"
                         :label="item.label"
                         :value="item.value"></el-option>
            </el-select>
          </el-form-item>
          <!-- <el-form-item label="渠道">
            <el-select v-model="formsearch.channel"
                       filterable
                       clearable
                       placeholder="请选择">
              <el-option v-for="item in channel_opt"
                         :key="item.id"
                         :label="item.id+'-'+item.value"
                         :value="item.id">{{item.id}}-{{item.value}}</el-option>
            </el-select>
          </el-form-item> -->
          <el-form-item label="买家">
            <el-input v-model="formsearch.buyer"
                      clearable></el-input>
          </el-form-item>
          <el-form-item>
            <el-button native-type="reset"
                       @click="onReset">重置</el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary"
                       native-type="button"
                       :loading="isLoading"
                       @click="getBuyer('click')"
                       icon="el-icon-search">搜索</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>

    <el-table v-loading="listLoading"
              :data="buyer_res"
              element-loading-text="Loading"
              border
              fit
              highlight-current-row>
      <el-table-column align="center"
                       label="USER_ID"
                       width="95">
        <template slot-scope="scope">
          {{ scope.row.user_id }}
        </template>
      </el-table-column>
      <el-table-column align="center"
                       label="USER_NAME"
                       width="160">
        <template slot-scope="scope">
          {{ scope.row.user_name }}
        </template>
      </el-table-column>
      <el-table-column label="PASSWD"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.passwd }}</span>
        </template>
      </el-table-column>
      <el-table-column label="ADDRESS"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.addresses }}</span>
        </template>
      </el-table-column>
      <!-- <el-table-column label="Pageviews"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          {{ scope.row.pageviews }}
        </template>
      </el-table-column>
      <el-table-column class-name="status-col"
                       label="Status"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column align="center"
                       prop="created_at"
                       label="Display_time"
                       width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template>
      </el-table-column> -->
    </el-table>
  </div>
</template>

<script>
import { getList } from '@/api/table'
import request_local from "@/utils/request_local";

export default {
  filters: {
    statusFilter (status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data () {
    return {
      list: null,
      listLoading: true,
      isLoading: false,
      // 下拉菜单值
      env_opt: [
        {
          value: "test",
          label: "TEST"
        },
        {
          value: "uat",
          label: "UAT"
        },
        {
          value: "staging",
          label: "STAGING"
        }
      ],
      country_opt: [
        {
          value: "ID",
          label: "ID"
        },
        {
          value: "VN",
          label: "VN"
        },
        {
          value: "TH",
          label: "TH"
        },
        {
          value: "MY",
          label: "MY"
        },
        {
          value: "SG",
          label: "SG"
        },
        {
          value: "PH",
          label: "PH"
        },
        {
          value: "TW",
          label: "TW"
        }
      ],
      channel_opt: [],
      buyer_res: null,
      formsearch: {
        env: '',
        country: '',
        channel: '',
        buyer: ''
      },
      rules: {
        env: [
          { required: true, message: '请选择环境', trigger: 'change' },
        ],
        country: [
          { required: true, message: '请选择国家', trigger: 'change' }
        ],
        channel: [
          { required: true, message: '请选择渠道', trigger: 'change' }
        ],
        buyer: [
          { required: false, message: '请输入买家' },
          // { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
        ]
      }

    }
  },
  created () {
    this.fetchData()
  },
  methods: {
    fetchData () {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data.items
        this.listLoading = false
      })
    },
    onReset () {
      this.formsearch.env = "";
      this.formsearch.country = "";
      // this.formsearch.channel = "";
      this.formsearch.buyer = "";
    },
    // getChannel () {
    //   this.formsearch.channel = "";
    //   var dat = {
    //     env: this.formsearch.env,
    //     country: this.formsearch.country
    //   };
    //   if (this.formsearch.env != "" && this.formsearch.country != "") {
    //     this.channel_opt = []; // 清空channel_opt
    //     console.log(dat);
    //     request_local.post("/tool/orderflow/channels/", JSON.stringify(dat))
    //       .then(response => {
    //         const channelData = response.data.data;
    //         console.log("channelData:===> ", channelData);
    //         for (var i = 0; i < channelData.length; i++) {
    //           this.channel_opt.push({
    //             id: channelData[i].channel_id,
    //             value: channelData[i].channel_name
    //           });
    //         }
    //         // 默认选择框值
    //         this.formsearch.channel = this.channel_opt[0].id + "-" + this.channel_opt[0].value;
    //       })
    //       .catch(error => {
    //         console.log(error);
    //       });
    //   }
    // },
    getBuyer (tag) {
      this.buyer_res = []
      var dat = {
        env: this.formsearch.env,
        country: this.formsearch.country
      };
      if (this.formsearch.env != "" && this.formsearch.country != "") {
        this.isLoading = true
        this.listLoading = true
        console.log(dat);
        request_local.post("/tool/orderflow/buyerdetail/", JSON.stringify(dat))
          .then(response => {
            const buyerData = response.data.data;
            console.log("buyerData:===> ", buyerData);
            for (var i = 0; i < buyerData.length; i++) {
              if (buyerData[i].user_name.search(this.formsearch.buyer) != -1) {
                this.buyer_res.push(buyerData[i])
              }
            }
            this.isLoading = false
            this.listLoading = false
            console.log("buyer_res:===> ", this.buyer_res);
          })
          .catch(error => {
            this.isLoading = false
            console.log(error);
          });
      } else if (tag == "click" && (this.formsearch.env == "" || this.formsearch.country == "")) {
        this.isLoading = false
        alert("请选择环境和国家")
      }
    },
  }
}
</script>
