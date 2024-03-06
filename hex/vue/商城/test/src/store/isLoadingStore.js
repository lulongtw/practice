

let isLoadingStore = {
  namespaced: true,
  state(){
    return{
      isLoading:false,
    }
  },
  mutations:{
    toggleLoading(state){
     
      state.isLoading = !state.isLoading
    }
  }
}

export default isLoadingStore