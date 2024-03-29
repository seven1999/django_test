'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  BASE_API: '"http://127.0.0.1:8001"', // 修改为'"https://api-prod"'就行了
  APP_ORIGIN: '"https://wallstreetcn.com"' // 为公司打个广告 pc站为vue+ssr
})
