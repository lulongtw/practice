export default {
  state(){
    return{
      isLoading:false
    }
  },
  mutations:{
    hideLoading(state){
      state.isLoading = false
    },
    showLoading(state){
      state.isLoading = true
    }
  }
}