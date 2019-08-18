<template>
  <el-form ref="form"
           :model="sizeForm"
           label-width="80px"
           size="mini">
    <br>
    <el-form-item label="shopid">
      <el-col :span="3">
        <el-input v-model="sizeForm.shopid"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="country">
      <el-col :span="3">
        <el-input v-model="sizeForm.country"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="itemid">
      <el-col :span="3">
        <el-input v-model="sizeForm.itemid"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="name">
      <el-col :span="3">
        <el-input v-model="sizeForm.name"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="price">
      <el-col :span="3">
        <el-input v-model="sizeForm.price"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="stock">
      <el-col :span="3">
        <el-input v-model="sizeForm.stock"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="status">
      <el-col :span="3">
        <el-input v-model="sizeForm.status"></el-input>
      </el-col>
    </el-form-item>
    <el-form-item label="desc">
      <el-col :span="3">
        <el-input v-model="sizeForm.description"></el-input>
      </el-col>
    </el-form-item>

    <el-form-item size="large">
      <el-button type="primary"
                 @click="onSubmit">立即创建</el-button>
      <el-button @click="onReset">重置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      sizeForm: {
        shopid: '',
        country: '',
        itemid: '',
        name: '',
        price: '',
        stock: '',
        status: '',
        description: ''
      }
    };
  },
  methods: {
    isNull(str){
      if (str == ""){
        return true
      }
      return false
    },
    onReset () {
      this.sizeForm.shopid = "";
      this.sizeForm.country = "";
      this.sizeForm.itemid = "";
      this.sizeForm.name = "";
      this.sizeForm.price = "";
      this.sizeForm.stock = "";
      this.sizeForm.status = "";
      this.sizeForm.description = "";
    },
    onSubmit () {
      var dat = {
        shopid: this.sizeForm.shopid,
        country: this.sizeForm.country,
        itemid: this.sizeForm.itemid,
        name: this.sizeForm.name,
        price: this.sizeForm.price,
        stock: Number(this.sizeForm.stock),
        status: Number(this.sizeForm.status),
        description: this.sizeForm.description
      };
      if(this.isNull(this.sizeForm.shopid) || this.isNull(this.sizeForm.country) ||this.isNull(this.sizeForm.itemid) ||this.isNull(this.sizeForm.name)  ||this.isNull(this.sizeForm.status)){
        alert("shopid, country, itemid, name and status should not be null")
      }else{
              axios.post("http://127.0.0.1:8002/api/addshop/", dat)
        .then(response => {
          const resultData = response.data;
          console.log("resultData:===> ", resultData);
          this.$message.success("addshop seccess!")
          this.onReset()
        })
        .catch(error => {
          this.$message.error("addshop fail!")
          console.log(error);
        });
      }
    }
  }
};
</script>