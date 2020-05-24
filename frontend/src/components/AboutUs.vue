<template>
  <div class="aboutUs">
    <img src="../assets/logo.png">
    <b-card-group
      deck>
      <b-card
        v-bind:key="item.title"
        v-for="item in aboutList"
        :title="item.title"
        img-src="http://localhost:8080/static/logo.png"
        :img-alt="item.imgAlt"
        img-top
        tag="article"
        style="max-width: 20rem"
        class="mb-2">
        <b-card-text
          align="left">
          {{item.text}}
        </b-card-text>
        <b-button
          :href="item.buttonLink"
          variant="success">
          Learn More
        </b-button>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'aboutUs',
  components: {},
  data () {
    return {
      aboutList: [
        {
          title: '关于日慈',
          imgSrc: '../assets/logo.png',
          imgAlt: 'rici-logo',
          text: '日慈公益基金会（全称“广东省日慈公益基金会”）' +
          '于2013年12月31日在广东省民政厅注册成立,' +
          '2014年正式开始运行,' +
          '是一个致力于青少年儿童心灵成长与幸福生活的非公募基金会,' +
          '2017年7月被评为广东省“AAA”级社会组织,' +
          '2017年12月被认定为慈善组织。',
          buttonLink: 'http://www.ricifoundation.org/index/about?id=1'
        },
        {
          title: '关于心灵魔法学院',
          imgSrc: '../assets/logo.png',
          imgAlt: 'magicAcademy-logo',
          text: '项目从预防视角出发,' +
          '通过赋能、培训教师,' +
          '于每学期在校园内为6-16岁青少年儿童提供9-12节心智素养课程。',
          buttonLink: 'http://www.ricifoundation.org/index/project?id=5'
        },
        {
          title: '关于心智素养课程',
          imgSrc: '../assets/logo.png',
          imgAlt: '电风扇',
          text: '基于社会情感学习理论和积极心理学研发设计的、' +
          '符合其年龄特点的参与式系列课程，' +
          '培养学生的自我认知能力、情绪管理能力、人际交往能力，' +
          '从而提高其心理抗逆力。',
          buttonLink: 'http://www.ricifoundation.org/index/project?id=8'
        }
      ]
    }
  },
  methond: {

  }
}
</script>
