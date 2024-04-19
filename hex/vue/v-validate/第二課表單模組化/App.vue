<script setup>
  import App1 from "@/App1.vue";
  import * as yup from "yup";

  /*
  這節課上父組件整坨資料迭代進子組件
  父組件負責建立  rules,name,type順便建立label 
  子組件負責接收而已
  */
  const schema = {
    fields:[
      { 
        label:'這是名字',
        name:'name',
        /*這邊的name重要性不像:valudation-schema直接設在Form上 有連結 rules  
       因為rules直接迭代進組件了
       這遍name負責連接label 的 for Field的id  以及errormsg的name
        */
        type:'text',
        as:'input',//指定Field作為input 
        rules:yup.string().required("名字必須").test(
          'noNum','沒有數字',val=>!/\d/.test(val)
        )
      },{
        label:'這是伊妹兒',
        name:'email',
        type:"email",
        as:'input',
        rules:yup.string().email('不合email').required('email必須')
      },{
        label:'這是密碼',
        name:'password',
        type:'text',
        as:'input',
        //yup.number無法自定errormsg 所以乾脆不用 因為錯誤會被擋下
        //直接用.test()
        rules:yup.string().required('必須密碼').min(3,'要超過3個').test(
          'numOnly','必須數字',val=>/\d/.test(val)

        )
      }
    ]
  }
</script>
<template>
  <App1 :fromDad="schema"></App1>
</template>