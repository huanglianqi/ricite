<template>
  <div
    id="course">
    <t-menu
      :tag-name-dropdown-title="tagTitle"
      :tag-name-dropdown-value="tagValue"
      :tag-name-select-item="selectTag"
      :term-num-dropdown-title="termTitle"
      :term-num-dropdown-value="termValue"
      :term-num-select-item="selectTerm"
      :search-keyword="keyword"
      :input-keyword="inputKeyword">
    </t-menu>
    <t-card-group>
      <b-card
        v-show="certain_tag_and_term_no_keyword"
        border-variant="success">
        <b-card-header
          header-bg-variant="success"
          header-text-variant="light"
          class="mb-4 font-weight-bolder border-0">
          <b-icon
            icon="star-fill"
            class="float-left"
            shift-v="-3">
          </b-icon>
          课程反馈 | 学期汇总
          <b-icon
            icon="star-fill"
            class="float-right"
            shift-v="-3">
          </b-icon>
        </b-card-header>
        <b-card-text
          class="text-left font-weight-bolder">
          <b-icon
            icon="calendar-check-fill"
            variant="success"
            class="mr-3">
          </b-icon>
          {{termTitle}}
        </b-card-text>
        <b-card-text
          class="text-left font-weight-bolder">
          <b-icon
            icon="book"
            variant="success"
            class="mr-3">
          </b-icon>
          {{tagTitle}}
        </b-card-text>
        <b-card-text
          class="text-left font-weight-bolder mt-4">
          <b-button
            block
            variant="outline-success"
            v-b-modal.summaryModal
            v-on:click="getSummary"
            :disabled="!teacherList_exist">
            <div
              v-show="teacherList_exist">
              <b-icon
                icon="card-checklist"
                class="float-left">
              </b-icon>
              查看反馈汇总
              <b-icon
                icon="box-arrow-up-right"
                class="float-right"
                shift-v="-0.5">
              </b-icon>
            </div>
            <div
              v-show="!teacherList_exist">
              <b-icon
                icon="card-checklist"
                class="float-left">
              </b-icon>
              暂无课程反馈
              <b-icon
                icon="cone-striped"
                class="float-right">
              </b-icon>
            </div>
          </b-button>
        </b-card-text>
      </b-card>
      <b-card
        v-for="item in teacherList"
        :key="item.id">
        <b-card-text
          class="text-left font-weight-bolder mt-4">
          <b-icon
            icon="person-fill"
            variant="success"
            class="mr-3">
          </b-icon>
          {{item.teacher}}
        </b-card-text>
        <b-card-text
          class="text-left font-weight-bolder">
          <b-icon
            icon="calendar-check-fill"
            variant="success"
            class="mr-3">
          </b-icon>
          {{term_readable(item.term_num)}}
        </b-card-text>
        <b-card-text
          class="text-left font-weight-bolder mb-3">
          <b-icon
            icon="book"
            variant="success"
            class="mr-3">
          </b-icon>
          {{tag_readable(item.tag_name)}}
        </b-card-text>
        <b-card-text
          class="text-left font-weight-bolder mt-3">
          <t-progress
            :max="item.course_num + 1"
            :value="item.feedback_forms.length">
          </t-progress>
        </b-card-text>
        <b-card-text
          class="mt-4 mb-2">
          <b-button
            block
            variant="outline-success"
            v-b-modal.formsModal
            v-on:click="formIdList = item.feedback_forms">
            <b-icon
              icon="card-checklist"
              class="float-left">
            </b-icon>
            查看课程反馈
            <b-icon
              icon="box-arrow-up-right"
              class="float-right"
              shift-v="-0.9">
            </b-icon>
          </b-button>
        </b-card-text>
      </b-card>
    </t-card-group>
    <t-modal
      :title="`${this.termTitle} ${this.tagTitle}`"
      id="formsModal">
      <b-jumbotron
        v-for="item in forms"
        :key="item.class_num"
        bg-variant="white"
        border-variant="info">
        <template
          v-slot:lead>
          <p
            class="font-weight-bold">
            {{course_readable(item.class_num)}}
          </p>
        </template>
        <b-icon
          icon="clock-history"></b-icon>
          {{time_readable(item.create_time)}}
        <hr>
        <div
          v-for="unit in item.feedback_units"
          :key="unit[0]">
          <p
            class="font-weight-light">
            <b-icon
              icon="question-circle-fill"
              variant="success"
              class="mr-3">
            </b-icon>
            {{unit[0]}}
          </p>
          <p
            class="font-weight-bolder">
            <b-icon
              icon="chat-quote-fill"
              variant="success"
              class="mr-3">
            </b-icon>
            {{unit[1]}}
          </p>
          <hr>
        </div>
        <b-button
          v-b-modal.checkPics
          variant="outline-success"
          v-on:click="picList=item.feedback_pics">
          查看反馈照片
          <b-badge
            variant="success">
            {{item.feedback_pics.length}}
          </b-badge>
        </b-button>
      </b-jumbotron>
    </t-modal>
    <t-modal
      :title="`${this.termTitle} ${this.tagTitle}`"
      id="checkPics">
      <b-carousel
        id="feedbackPicCheck"
        v-model="slide"
        controls
        indicators
        background="#ababab"
        img-width="512"
        img-height="240"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd">
        <b-carousel-slide
          v-for="url in picList"
          :key="url"
          :img-src="url">
        </b-carousel-slide>
      </b-carousel>
    </t-modal>
    <t-modal
      :title="`${this.termTitle} ${this.tagTitle}`"
      id="summaryModal">
      <t-card-group>
        <b-card
          v-for="item in courseNum"
          :key="item">
          <b-card-text>
            <b-button
              block
              variant="outline-success"
              v-b-modal.courseModal
              v-on:click="summaryItem=summary[item - 1]">
              <b-icon
                icon="box-arrow-up-right"
                class="float-right">
              </b-icon>
              <b-icon
                icon="card-checklist"
                class="float-left">
              </b-icon>
              {{course_readable(item - 1)}}
            </b-button>
          </b-card-text>
        </b-card>
      </t-card-group>
    </t-modal>
    <t-modal
      id="courseModal"
      :title="`${this.termTitle} ${this.tagTitle} ${this.course_readable(this.summaryItem.course)}`">
      <div
        v-if="summaryItem.units !== null">
        <b-jumbotron
          bg-variant="white"
          border-variant="info"
          v-for="unit in summaryItem.units"
          :key="unit.question">
          <div
            v-if="unit.question === '姓名'">
            <p
              class="font-weight-light">
              感谢以下填写该反馈问卷的老师
            </p>
            <b-button
              size="sm"
              v-on:click="getFormsIdList(answer.userId)"
              v-b-modal.formsModal
              variant="outline-success"
              class="mr-2 mb-2"
              v-for="answer in unit.answers"
              :key="`${answer.teacher}:${answer.content}`">
              <b-icon
                icon="at">
              </b-icon>
              {{answer.content}}
            </b-button>
          </div>
          <div
            v-else>
            <p
              class="font-weight-light">
              {{unit.question}}
            </p>
            <hr>
            <b-container
              v-for="answer in unit.answers"
              :key="`${answer.teacher}:${answer.content}`">
              <b-row>
                <b-col>
                  <b-button
                    v-on:click="getFormsIdList(answer.userId)"
                    v-b-modal.formsModal
                    variant="outline-success"
                    class="mr-2 mb-1 mt-1"
                    size="sm">
                    <b-icon
                      icon="at">
                    </b-icon>
                    {{answer.teacher}}
                  </b-button>
                </b-col>
                <b-col>
                  <p
                    class="font-weight-border">
                    {{answer.content}}
                  </p>
                </b-col>
              </b-row>
            </b-container>
          </div>
        </b-jumbotron>
      </div>
      <div
        v-else>
        没有反馈哦的图片
      </div>
    </t-modal>
    <div
      v-show="overOffset">
      <hr>
      Oops! 没有了
    </div>
  </div>
</template>

<script>
import Axios from 'axios'
import ToolMenuVue from './ToolMenu.vue'
import ToolCardGroupVue from './ToolCardGroup.vue'
import ToolProgressVue from './ToolProgress.vue'
import ToolModalVue from './ToolModal.vue'

export default {
  name: 'course',
  components: {
    't-menu': ToolMenuVue,
    't-card-group': ToolCardGroupVue,
    't-progress': ToolProgressVue,
    't-modal': ToolModalVue
  },
  data () {
    return {
      tagTitle: '--请选择课程--',
      tagValue: null,
      tagMark: null,
      termTitle: '--请选择学期--',
      termValue: null,
      termMark: null,
      keyword: '',
      teacherList: [],
      forms: [],
      formIdList: [],
      picList: [],
      slide: 0,
      sliding: null,
      courseNum: 0,
      bottom: false,
      offset: 0,
      overOffset: false,
      summary: [],
      summaryItem: {}
    }
  },
  created () {
    window.addEventListener(
      'scroll',
      () => {
        this.bottom = this.bottomVisible()
      }
    )
  },
  watch: {
    bottom (bottom) {
      if (bottom) {
        this.offset += 50
        this.getTeacherList(
          this.tagValue,
          this.termValue,
          this.offset
        )
      }
    },
    termValue (term) {
      if (this.tagValue !== null) {
        this.teacherList = []
        this.offset = 0
        this.overOffset = false
        this.getTeacherList(this.tagValue, term, this.offset)
      }
    },
    tagValue (tag) {
      if (this.termValue !== null) {
        this.teacherList = []
        this.offset = 0
        this.overOffset = false
        this.getTeacherList(tag, this.termValue, this.offset)
      }
    },
    teacherList (list) {
      for (let i = 0; i < list.length; i++) {
        this.getTeacherName(list[i].teacher, i)
      }
      if (list.length !== 0) {
        this.courseNum = list[0].course_num + 1
      }
    },
    forms (form) {
      this.orderForms(form)
    },
    formIdList (list) {
      this.forms = []
      list.forEach(
        this.getForms
      )
    },
    feedback_forms_items (items) {
      this.get_feedback_forms(items)
    },
    keyword (keyword) {
      console.log(keyword)
    }
  },
  computed: {
    certain_tag_and_term_no_keyword () {
      if (this.keyword === '') {
        if (this.termValue === null || this.tagValue === null || this.termValue === '' || this.tagValue === '') {
          return false
        } else {
          return true
        }
      } else {
        return false
      }
    },
    teacherList_exist () {
      if (this.teacherList.length === 0) {
        return false
      } else {
        return true
      }
    }
  },
  methods: {
    // search func
    inputKeyword (keyword) {
      this.keyword = keyword
    },
    // readable
    time_readable (time) {
      return `${time.split('T')[0]}(${time.split('T')[1].split('+')[0]})`
    },
    course_readable (num) {
      if (num === 0 || num === '0') {
        return '结课反馈'
      } else {
        return `课时 ${num}`
      }
    },
    term_readable (num) {
      if (num % 2 === 0) {
        return (num / 2 + 2019) + '年春季学期'
      } else {
        return (num / 2 - 0.5 + 2019) + '年秋季学期'
      }
    },
    tag_readable (tag) {
      return tag.split('【')[0]
    },
    // get (individual) forms
    splitQA (units) {
      let ls = []
      for (let i = 0; i < units.length; i++) {
        ls.push(
          [
            units[i].split(':')[0],
            units[i].split(':')[1]
          ]
        )
      }
      return ls
    },
    getForms (formId) {
      Axios
        .get(
          `flourish/feedback_form_detail/${formId}`
        )
        .then(
          res => {
            this.forms.push(
              {
                'class_num': res.data.class_num,
                'create_time': res.data.create_time,
                'feedback_units': this.splitQA(
                  res.data.feedback_units
                ),
                'feedback_pics': res.data.feedback_pics
              }
            )
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.auto_login()
              this.getForms(formId)
            }
          }
        )
    },
    bottomVisible () {
      const scrollY = window.scrollY
      const visible = document.documentElement.clientHeight
      const pageHeight = document.documentElement.scrollHeight
      const bottomOfPage = visible + scrollY >= pageHeight
      return bottomOfPage || pageHeight < visible
    },
    // get (partly) teacherList
    selectTerm (title, value) {
      this.termTitle = title
      this.termValue = value
    },
    selectTag (title, value) {
      this.tagTitle = title
      this.tagValue = value
    },
    getTeacherList (tag, term, offset) {
      Axios
        .get(
          `flourish/user_course/?offset=${offset}&limit=50&user_id=&tag_name=${tag}&term_num=${term}`
        )
        .then(
          res => {
            for (let i = 0; i < res.data.results.length; i++) {
              if (res.data.results[i].feedback_forms.length === 0) {
                continue
              } else {
                this.teacherList.push(res.data.results[i])
              }
            }
            if (offset > res.data.count) {
              this.overOffset = true
            }
          }
        )
        .catch(
          err => {
            if (String(err).indexOf('401')) {
              this.auto_login()
              this.getTeacherList(tag, term, offset)
            }
          }
        )
    },
    getTeacherName (id, position) {
      if (typeof this.teacherList[position].teacher === 'number') {
        Axios
          .get(
            `flourish/detail/${id}`
          )
          .then(
            res => {
              this.teacherList[position].teacher = res.data.real_name
            }
          )
          .catch(
            err => {
              if (err) {
                if (String(err).indexOf('401')) {
                  this.auto_login()
                  this.getTeacherName(id, position)
                }
              }
            }
          )
      }
    },
    getSummary () {
      if (this.tagMark !== null && this.termMark !== null) {
        if (this.tagValue !== this.tagMark || this.termValue !== this.termMark) {
          this.summary = []
          this.getSummary_detail()
          this.tagMark = this.tagValue
          this.termMark = this.termValue
        }
      } else {
        this.tagMark = this.tagValue
        this.termMark = this.termValue
        this.summary = []
        this.getSummary_detail()
      }
    },
    getSummary_detail () {
      let count = 0
      Axios
        .get(`flourish/user_course/?limit=1`)
        .then(
          res => {
            count = res.count
            Axios
              .get(
                `flourish/user_course/?limit=${count}&term_num=${this.termValue}&tag_name=${this.tagValue}`
              )
              .then(
                res => {
                  this.summaryGenerator(res.data.results[0].course_num)
                  for (let i = 0; i < res.data.results.length; i++) {
                    if (res.data.results[i].feedback_forms.length !== 0) {
                      this.getIndividualForms(res.data.results[i].feedback_forms)
                    }
                  }
                }
              )
              .catch(
                err => {
                  if (String(err).indexOf('401')) {
                    this.auto_login()
                    this.getSummary_detail()
                  }
                }
              )
          }
        )
    },
    getIndividualForms (formsIdList) {
      for (let i = 0; i < formsIdList.length; i++) {
        Axios
          .get(
            `flourish/feedback_form_detail/${formsIdList[i]}`
          )
          .then(
            res => {
              for (let k = 0; k < this.summary.length; k++) {
                if (String(this.summary[k].course) === res.data.class_num) {
                  if (this.summary[k].units.length === 0) {
                    for (let j = 0; j < res.data.feedback_units.length; j++) {
                      this.summary[k].units.push(
                        {
                          question: this.splitIndividualQA(res.data.feedback_units[j])[0],
                          answers: [
                            {
                              teacher: this.splitIndividualQA(res.data.feedback_units[0])[1],
                              userId: res.data.user_id,
                              content: this.splitIndividualQA(res.data.feedback_units[j])[1]
                            }
                          ]
                        }
                      )
                    }
                  } else {
                    for (let j = 0; j < this.summary[k].units.length; j++) {
                      for (let n = 0; n < res.data.feedback_units.length; n++) {
                        if (this.splitIndividualQA(res.data.feedback_units[n])[0] === this.summary[k].units[j].question) {
                          this.summary[k].units[j].answers.push(
                            {
                              teacher: this.splitIndividualQA(res.data.feedback_units[0])[1],
                              userId: res.data.user_id,
                              content: this.splitIndividualQA(res.data.feedback_units[n])[1]
                            }
                          )
                        }
                      }
                    }
                  }
                }
              }
            }
          )
      }
    },
    summaryGenerator (num) {
      for (let i = 0; i < num + 1; i++) {
        this.summary.push(
          {
            course: i,
            units: []
          }
        )
      }
    },
    splitIndividualQA (qa) {
      return [qa.split(':')[0], qa.split(':')[1]]
    },
    getFormsIdList (userId) {
      Axios
        .get(
          `flourish/user_course/?user_id=${userId}&term_num=${this.termValue}&tag_name=${this.tagValue}`
        )
        .then(
          res => {
            this.formIdList = res.data.results[0].feedback_forms
          }
        )
    },
    auto_login () {
      this.$store
        .dispatch(
          'auth/login',
          {
            username: sessionStorage.username,
            password: sessionStorage.password
          }
        )
    },
    onSlideStart (slide) {
      this.sliding = true
    },
    onSlideEnd (slide) {
      this.sliding = false
    },
    orderForms (form) {
      for (let i = 1; i < form.length; i++) {
        var key = form[i].class_num
        var value = form[i]
        var j = i - 1
        while (j >= 0 && form[j].class_num > key) {
          form[j + 1] = form[j]
          j = j - 1
        }
        form[j + 1] = value
      }
    },
    logout () {
      this.$store
        .dispatch('auth/logout')
        .then(
          this.$router.push('/login')
        )
        .catch(
          err => (console.log(err))
        )
    }
  }
}
</script>

<style>

</style>
