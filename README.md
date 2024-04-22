自己用的python工具
====


Overview
----

基于 [Ant Design of Vue](https://vuecomponent.github.io/ant-design-vue/docs/vue/introduce-cn/) 实现的 Ant Design Pro  Vue 版
Jeecg-boot 的前段UI框架，采用前后端分离方案，提供强大代码生成器的快速开发平台。
前端页面代码和后端功能代码一键生成，不需要写任何代码，保持jeecg一贯的强大！！



#### 前端技术
 
- 基础框架：[ant-design-vue](https://github.com/vueComponent/ant-design-vue) - Ant Design Of Vue 实现
- JavaScript框架：Vue
- Webpack
- node
- yarn
- eslint
- @vue/cli 3.2.1
- [vue-cropper](https://github.com/xyxiao001/vue-cropper) - 头像裁剪组件
- [@antv/g2](https://antv.alipay.com/zh-cn/index.html) - Alipay AntV 数据可视化图表
- [Viser-vue](https://viserjs.github.io/docs.html#/viser/guide/installation)  - antv/g2 封装实现



项目下载和运行
----

- 拉取项目代码
```bash
git clone https://github.com/zhangdaiscott/jeecg-boot.git
cd  jeecg-boot/ant-design-jeecg-vue
```

- 安装依赖
```
yarn install
```

- 开发模式运行
```
yarn run serve
```

- 编译项目
```
yarn run build
```

- Lints and fixes files
```
yarn run lint
```



其他说明
----

- 项目使用的 [vue-cli3](https://cli.vuejs.org/guide/), 请更新您的 cli

- 关闭 Eslint (不推荐) 移除 `package.json` 中 `eslintConfig` 整个节点代码

- 修改 Ant Design 配色，在文件 `vue.config.js` 中，其他 less 变量覆盖参考 [ant design](https://ant.design/docs/react/customize-theme-cn) 官方说明
```ecmascript 6
  css: {
    loaderOptions: {
      less: {
        modifyVars: {
          /* less 变量覆盖，用于自定义 ant design 主题 */

          'primary-color': '#F5222D',
          'link-color': '#F5222D',
          'border-radius-base': '4px',
        },
        javascriptEnabled: true,
      }
    }
  }
```



附属文档
----
- [Ant Design Vue](https://vuecomponent.github.io/ant-design-vue/docs/vue/introduce-cn)

- [报表 viser-vue](https://viserjs.github.io/demo.html#/viser/bar/basic-bar)

- [Vue](https://cn.vuejs.org/v2/guide)

- [路由/菜单说明](https://github.com/zhangdaiscott/jeecg-boot/tree/master/ant-design-jeecg-vue/src/router/README.md)

- [ANTD 默认配置项](https://github.com/zhangdaiscott/jeecg-boot/tree/master/ant-design-jeecg-vue/src/defaultSettings.js)

- 其他待补充...


备注
----

> @vue/cli 升级后，eslint 规则更新了。由于影响到全部 .vue 文件，需要逐个验证。既暂时关闭部分原本不验证的规则，后期维护时，在逐步修正这些 rules


Docker 镜像使用
----

 ``` 
# 1.修改前端项目的后台域名
    .env.development
    域名改成： http://jeecg-boot-system:8080/jeecg-boot
   
# 2.先进入打包前端项目
  yarn run build

# 3.构建镜像
  docker build -t nginx:jeecgboot .

# 4.启动镜像
  docker run --name jeecg-boot-nginx -p 80:80 -d nginx:jeecgboot

# 5.配置host

    # jeecgboot
    127.0.0.1   jeecg-boot-redis
    127.0.0.1   jeecg-boot-mysql
    127.0.0.1   jeecg-boot-system
  
# 6.访问前台项目
  http://localhost:80

# 7.埃维网上营业厅改动  差异

    # src\views\dashboard\Analysis.vue
      src\components\page\GlobalHeader.vue
      src\components\tools\Logo.vue
      src\views\user\Login.vue
      src\components\page\GlobalFooter.vue
      src\components\JMoreOperat\JMoreOperat.vue
      src\views\workOrder\BizWorkorderBusList.vue
    props属性中 aiwei字段区分  ('aiwei' = 埃维营业厅  '' = 锋云慧ibs)  

    # public\index.html
    vue设置浏览器顶部小图标的切换   加载动画文字提示 (页面底部)

  # 8.上传组件字段分析
      "itemAllowDelete": false,       // 元素是否可删除
      "editWay": "2,2,2",             // 从左至右表示app,web,小程序   数字含义 1必填 2选填 3隐藏
      "param": "BusinessLicense",     // 对应图片在数据库中存储的字段名
      "uploadWay": 1,                 // 文件的上传方式 1本地上传 2高拍仪 3本地上传/高拍仪 空值表示本地上传
      "maxSize": 10240,               // 支持的图片大小
      "title": "营业执照12",           // 图片的类型名称 
      "type": "jpg,png,jpeg",         // 支持的图片类型
      "fileName": ""                  // 文件上传后服务器返回的路径


  docker run --name jeecg-boot-nginx -p 80:80 -d nginx:jeecgboot
``` 


###  多图组件展示UploadManyWay
后端返回格式有老数据存在又有新json类型的图片数据返回时
如：1、"/000000/repairPic/IMG_CMP_365421_30084012_1666753801765.jpg,/000000/repairPic/IMG_CMP_365421_30084012_1666753801712.jpg";
2、"{\"max\":2,\"list\":[{\"itemAllowDelete\":false,\"editWay\":\"2,2,2\",\"param\":\"materialOne\",\"title\":\"附件1\",\"maxSize\":10240,\"type\":\"jpg,png,jpeg\",\"fileName\":\"\"},{\"itemAllowDelete\":false,\"editWay\":\"2,2,2\",\"param\":\"materialTwo\",\"maxSize\":10240,\"title\":\"附件2\",\"type\":\"jpg,png,jpeg\",\"fileName\":\"\"}]}"

可参考方法：handelManyType()
   
### 获取登录的用户信息   
this.$store.getters.userInfo.companyCode

### 如何配置增加一个自定义控件
（2023/8/4 赵以宝)
1. 开发相应的控件，请注意要支持双向绑定
2. 用编辑器打开node_modules\@jeecg\anti-online-mini\dist\OnlineForm.umd.min.js, 注意，不要改动格式
2. 搜索 "联动组件"，找到系统支持的控件列表，按照相应的格式，添加一个控件
3. 保存
4. 修改相应的模版form.vuei, 添加你的组件，即可生成带相应控件的页面
5. 注意：添加的组件在online开发中的功能测试中不工作。