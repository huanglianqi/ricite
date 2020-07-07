# flourish app

> api for flourish db

## Get API for VolunteerManagement.vue page

```javascript
/* Return parameter model:
 * res.data.results: Array
 * res.data.results[i].id: Number
 * res.data.results[i].user_course_id: String
 * res.data.results[i].user_id: String
 * res.data.results[i].tag_name: String
 * res.data.results[i].course_num: Number
 * res.data.results[i].term_num: String
 * res.data.results[i].teacher: Object
 * res.data.results[i].teacher.name: String
 * res.data.results[i].teacher.real_name: String
 * res.data.results[i].teacher.phone: String
 * res.data.results[i].teacher.user_id: String
 * res.data.results[i].teacher.head_img: <String: url>
 * res.data.results[i].teacher.create_time: <String: time>
 * res.data.results[i].teacher.is_fake: Boolean
 * res.data.results[i].teacher.has_course: Boolean
 * res.data.results[i].teacher.is_reapply: Boolean
 * res.data.results[i].teacher.active: Boolean
 * res.data.results[i].teacher.infoForms: Array
 * res.data.results[i].teacher.infoForms[i]: Object
 * res.data.results[i].teacher.infoForms[i].field_name: String
 * res.data.results[i].teacher.infoForms[i].field_value: String
*/

/*
 * get the list of
 * teachers who have course
 * but not sign protocal
 * in certain term
*/
axios
  .get(
    `${baseURL}flourish/no_protocal_list/${term}/`
  )

/*
 * get the list of
 * teacher who have not feedback for course
 * in certain term
*/
axios
  .get(
    `${baseURL}flourish/no_feedback_list/${term}/`
  )

/*
 * get the list of
 * teachers who have NOT totally completed all feedback forms
 * in certain term
*/
axios
  .get(
    `${baseURL}flourish/no_all_feedback_list/${term}/`
  )

/*
 * get the list of
 * teachers who have totally completed all feedback forms
 * in certain term
*/
aixos
  .get(
    `${baseURL}flourish/is_all_feedback_list/${term}/`
  )
```
