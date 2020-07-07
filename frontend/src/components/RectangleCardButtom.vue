<template>
  <div
    id="rectangleCardButtom">
    <div
      id="desktop"
      class="my-5">
      <b-container
        class="mx-5">
        <b-row>
          <b-col>
            <div
              v-for="item in processList"
              :key="item.titile"
              class="shadow-sm bg-white mb-3 p-3">
              <div
                v-on:click="getprocessDetail(item.content)">
                <b-row
                  class="mb-3 mt-1">
                  <b-col
                    class="text-left font-weight-bolder">
                    <b-icon
                      icon="circle-fill"
                      :variant="item.variant">
                    </b-icon>
                    {{item.title}}
                    <b-badge
                      class="float-right"
                      :variant="item.variant">
                      <b-icon
                        icon="people-fill">
                      </b-icon>
                      {{item.value}} | {{(item.value / allPeerNum * 100).toFixed(2)}}%
                    </b-badge>
                  </b-col>
                </b-row>
                <b-row
                  class="mb-1">
                  <b-col>
                    <b-progress
                      class="align-middle"
                      :max="allPeerNum"
                      :value="item.value"
                      :variant="item.variant">
                    </b-progress>
                  </b-col>
                </b-row>
              </div>
            </div>
          </b-col>
          <b-col
            class="font-weight-bolder mt-4">
            <b-row
              class="mb-3">
              <div
                v-on:click="getSummaryDetail(summaryList[0].content)">
                <b-col
                  class="shadow-sm bg-white p-5 mx-3">
                  <b-row>
                    <b-col
                      class="text-warning">
                      <h1>
                        {{summaryList[0].value}}
                      </h1>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      {{summaryList[0].title}}
                    </b-col>
                  </b-row>
                </b-col>
              </div>
              <div
                v-on:click="getSummaryDetail(summaryList[1].content)">
                <b-col
                  class="shadow-sm bg-white p-5 mx-3">
                  <b-row>
                    <b-col
                      class="text-danger">
                      <h1>
                        {{summaryList[1].value}}
                      </h1>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      {{summaryList[1].title}}
                    </b-col>
                  </b-row>
                </b-col>
              </div>
            </b-row>
            <b-row
              class="mb-3">
              <div
                v-on:click="getSummaryDetail(summaryList[2].content)">
                <b-col
                  class="shadow-sm bg-white p-5 mx-3">
                  <b-row>
                    <b-col
                      class="text-info">
                      <h1>
                        {{summaryList[2].value}}
                      </h1>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      {{summaryList[2].title}}
                    </b-col>
                  </b-row>
                </b-col>
              </div>
              <div
                v-on:click="getSummaryDetail(summaryList[3].content)">
                <b-col
                  class="shadow-sm bg-white p-5 mx-3">
                  <b-row>
                    <b-col
                      class="text-success">
                      <h1>
                        {{summaryList[3].value}}
                      </h1>
                    </b-col>
                  </b-row>
                  <b-row>
                    <b-col>
                      {{summaryList[3].title}}
                    </b-col>
                  </b-row>
                </b-col>
              </div>
            </b-row>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div
      id="mobile"
      class="my-5">
      <b-container
        class="bv-example-row my-3">
        <div
          v-on:click="getSummaryDetail(summaryList[0].content)">
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-white p-5 mx-3">
              <b-row>
                <b-col
                  class="text-warning">
                  <h1>
                    {{summaryList[0].value}}
                  </h1>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  {{summaryList[0].title}}
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <div
          v-on:click="getSummaryDetail(summaryList[1].content)">
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-white p-5 mx-3">
              <b-row>
                <b-col
                  class="text-danger">
                  <h1>
                    {{summaryList[1].value}}
                  </h1>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  {{summaryList[1].title}}
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <div
          v-on:click="getSummaryDetail(summaryList[2].content)">
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-white p-5 mx-3">
              <b-row>
                <b-col
                  class="text-info">
                  <h1>
                    {{summaryList[2].value}}
                  </h1>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  {{summaryList[2].title}}
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <div
          v-on:click="getSummaryDetail(summaryList[3].content)">
          <b-row
            class="font-weight-bolder my-3">
            <b-col
              class="shadow-sm bg-white p-5 mx-3">
              <b-row>
                <b-col
                  class="text-success">
                  <h1>
                    {{summaryList[3].value}}
                  </h1>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  {{summaryList[3].title}}
                </b-col>
              </b-row>
            </b-col>
          </b-row>
        </div>
        <b-row>
          <b-col>
            <div
              v-for="item in processList"
              :key="item.title"
              class="shadow-sm bg-white mb-3 p-3">
              <div
                v-on:click="getProcessDetail(item.content)">
                <b-row
                  class="mb-3 mt-1">
                  <b-col
                    class="text-left font-weight-bolder">
                    <b-icon
                      icon="circle-fill"
                      :variant="item.variant">
                    </b-icon>
                    {{item.title}}
                    <b-badge
                      class="float-right"
                      :variant="item.variant">
                      <b-icon
                        icon="people-fill">
                      </b-icon>
                      {{item.value}} | {{(item.value / allPeerNum * 100).toFixed(2)}}%
                    </b-badge>
                  </b-col>
                </b-row>
                <b-row
                  class="mb-1">
                  <b-col>
                    <b-progress
                      class="align-middle"
                      :max="allPeerNum"
                      :value="item.value"
                      :variant="item.variant">
                    </b-progress>
                  </b-col>
                </b-row>
              </div>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  name: 'rectangleCardButtom',
  props: {
    processList: {
      type: Array,
      required: true,
      default: () => {
        return [
          {
            title: '未签署协议',
            value: 0,
            variant: 'danger',
            content: []
          },
          {
            title: '已签署协议但未课程反馈',
            value: 0,
            variant: 'warning',
            content: []
          },
          {
            title: '参与课程反馈但未结课',
            value: 0,
            variant: 'info',
            content: []
          },
          {
            title: '已结课',
            value: 0,
            variant: 'success',
            content: []
          }
        ]
      }
    },
    getProcessDetailFunc: {
      type: Function,
      required: true
    },
    summaryList: {
      type: Array,
      required: true,
      default: () => {
        return [
          {
            title: '已签署协议',
            value: 0,
            variant: 'text-warning',
            content: []
          },
          {
            title: '已审核通过',
            value: 0,
            variant: 'text-danger',
            content: []
          },
          {
            title: '参与课程反馈',
            value: 0,
            variant: 'text-info',
            content: []
          },
          {
            title: '预计结课率',
            value: '',
            variant: 'text-success',
            content: []
          }
        ]
      }
    },
    getSummaryDetailFunc: {
      type: Function,
      required: true
    },
    allPeerNum: {
      type: Number,
      required: true
    }
  },
  methods: {
    getProcessDetail (content) {
      this.getProcessDetailFunc(content)
    },
    getSummaryDeail (content) {
      this.getSummaryDetailFunc(content)
    }
  }
}
</script>

<style>
#mobile {
  display: none;
}
@media screen and (max-width: 850px) {
  #desktop {
    display: none;
  }
  #mobile {
    display: block;
  }
  #mobile > * {
    display: block;
  }
}
</style>
