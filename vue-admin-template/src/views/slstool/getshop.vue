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
                       @change="getChannelAndBuyer"
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
                       @change="getChannelAndBuyer"
                       filterable
                       clearable
                       placeholder="请选择">
              <el-option v-for="item in country_opt"
                         :key="item.value"
                         :label="item.label"
                         :value="item.value"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="渠道">
            <el-select v-model="formsearch.channel"
                       @change="getSellers"
                       filterable
                       clearable
                       placeholder="请选择">
              <el-option v-for="item in channel_opt"
                         :key="item.id"
                         :label="item.id+'-'+item.value"
                         :value="item.id">{{item.id}}-{{item.value}}</el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="卖家">
            <el-select v-model="formsearch.seller"
                       filterable
                       clearable
                       placeholder="请选择">
              <el-option v-for="item in seller_opt"
                         :key="item.value"
                         :label="item.name"
                         :value="item.userid">{{item.name}}</el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button native-type="reset"
                       @click="onReset">重置</el-button>
          </el-form-item>
          <el-form-item>
            <el-button type="primary"
                       native-type="button"
                       :loading="isLoading"
                       @click="getShopdetail"
                       icon="el-icon-search">搜索</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>

    <el-table v-loading="listLoading"
              :data="shop_res"
              element-loading-text="Loading"
              border
              fit
              highlight-current-row>
      <el-table-column align="center"
                       label="SHOPID"
                       width="95">
        <template slot-scope="scope">
          {{ shopid }}
        </template>
      </el-table-column>
      <el-table-column align="center"
                       label="COUNTRY"
                       width="110">
        <template slot-scope="scope">
          {{ scope.row.country }}
        </template>
      </el-table-column>
      <el-table-column label="ITEMID"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.itemid }}</span>
        </template>
      </el-table-column>
      <el-table-column label="NAME"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="PRICE"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.price }}</span>
        </template>
      </el-table-column>
      <el-table-column label="STOCK"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.stock }}</span>
        </template>
      </el-table-column>
      <el-table-column label="SKU"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.sku }}</span>
        </template>
      </el-table-column>
      <el-table-column label="STATUS"
                       width="110"
                       align="center">
        <template slot-scope="scope">
          <!-- <span>{{ scope.row.status }}</span> -->
          <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="DESCRIPTION"
                       align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.description }}</span>
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
        1: 'success',
        0: 'gray',
        2: 'danger'
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
      shop_res: null,
      buyer_opt: [],
      seller_opt: [],
      channel_data: [],
      shopid: "",
      formsearch: {
        env: '',
        country: '',
        channel: '',
        buyer: '',
        seller: ""
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
      this.formsearch.channel = "";
      this.formsearch.buyer = "";
    },
    strCup (str) {
      // 处理 id和name拼接以后 （id-name）截取id
      if (str != "") { return str.toString().split("-")[0] }
      return str
    },
    channelDataFun (data_str) {
      // console.log(data_str)
      for (var item in this.channel_opt) {
        if (this.channel_opt[item].value == data_str) {
          return this.channel_opt[item].id
        }
      }
      return data_str
    },
    sellerDataFun (data_str) {
      // console.log(data_str)
      for (var item in this.seller_opt) {
        if (this.seller_opt[item].name == data_str) {
          return this.seller_opt[item].userid
        }
      }
      return data_str
    },
    getChannelAndBuyer () {
      this.formsearch.channel = "";
      var dat = {
        env: this.formsearch.env,
        country: this.formsearch.country
      };
      if (this.formsearch.env != "" && this.formsearch.country != "") {
        this.channel_opt = []; // 清空channel_opt
        console.log(dat);
        request_local.post("/tool/orderflow/channels/", JSON.stringify(dat))
          .then(response => {
            const channelData = response.data.data;
            this.channel_data = channelData;
            console.log("channelData:===> ", channelData);
            for (var i = 0; i < channelData.length; i++) {
              this.channel_opt.push({
                id: channelData[i].channel_id,
                value: channelData[i].channel_name
              });
            }
            // 默认选择框值
            this.formsearch.channel = this.channel_opt[0].id + "-" + this.channel_opt[0].value;
            this.seller_opt = channelData[0].related_shop;
            if (this.seller_opt != "") {
              this.formsearch.seller = this.seller_opt[0].name;
              this.getShopdetail();       // 选择完后默认执行查询
            }
          })
          .catch(error => {
            console.log(error);
          });

        request_local.post("/tool/orderflow/buyerdetail/", JSON.stringify(dat))
          .then(response => {
            const buyerData = response.data.data;
            console.log("buyerData:===> ", buyerData);
            for (var i = 0; i < buyerData.length; i++) {
              // if (buyerData[i].user_name.search(this.formsearch.buyer) != -1) {
              //   this.shop_res.push(buyerData[i])
              // }
              this.buyer_opt.push({
                user_id: buyerData[i].user_id,
                user_name: buyerData[i].user_name,
              });
            }
            // 默认选择框值
            this.formsearch.buyer = this.buyer_opt[0].user_name
            console.log("buyer_opt:===> ", this.buyer_opt);
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    getShopdetail () {
      this.isLoading = true
      this.listLoading = true
      this.shop_res = []
      var dat = {
        env: this.formsearch.env,
        country: this.formsearch.country,
        userid: Number(this.sellerDataFun(this.formsearch.seller)),
        channelid: Number(this.strCup(this.formsearch.channel))
      };
      request_local.post("/tool/orderflow/shopdetail/", dat)
        .then(response => {
          var shop_data = response.data.data;
          console.log(shop_data)
          this.shopid = shop_data.shop_id      // shopid..  目前一个seller只有一个shop
          this.shop_res = shop_data.items
          // 停止loading
          this.isLoading = false
          this.listLoading = false
        })
        .catch(error => {
          console.log(error);
        });
    },
    getSellers () {
      this.seller = ""
      this.seller_opt = [];
      for (var item in this.channel_data) {
        console.log("this.channel_data[item].channel_id===>:", this.channel_data[item].channel_id)
        console.log("formsearch.channel_id===>:", this.formsearch.channel)
        if (this.channel_data[item].channel_id === this.formsearch.channel) {
          this.seller_opt = this.channel_data[item].related_shop;
          console.log(this.seller_opt);
          // 默认选择框值处理
          if (this.seller_opt != "") {
            this.formsearch.seller = this.seller_opt[0].name;
            this.getShopdetail();       // 选择完后默认执行查询
          }
        }
      }
    }
  }
}
</script>
