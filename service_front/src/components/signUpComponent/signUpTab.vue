<template>
  <div class="tab-wrap">
    <div :class="['join-tab', isActive[$store.state.signUpTabName][0]]" v-if="$store.state.signUpTabName">
      <div class="join-tab-flex">
        <img src="https://web-staging.brandi.co.kr/static/3.50.7/images/ic-join-step-01-s@3x.png" />
        <span>본인인증</span>
      </div>
    </div>

    <div :class="['join-tab', isActive[$store.state.signUpTabName][1]]" v-if="$store.state.signUpTabName">
      <div class="join-tab-flex">
        <img src="https://web-staging.brandi.co.kr/static/3.50.7/images/ic-join-step-02-40-s@3x.png" />
        <span>정보수집동의</span>
      </div>
    </div>

    <div :class="['join-tab', isActive[$store.state.signUpTabName][2]]" v-if="$store.state.signUpTabName">
      <div class="join-tab-flex">
        <img src="https://web-staging.brandi.co.kr/static/3.50.7/images/ic-join-step-03-40-s@3x.png" />
        <span>정보입력</span>
      </div>
    </div>

    <div :class="['join-tab', isActive[$store.state.signUpTabName][3]]" v-if="$store.state.signUpTabName">
      <div class="join-tab-flex">
        <img src="https://web-staging.brandi.co.kr/static/3.50.7/images/ic-join-step-04-s@3x.png" />
        <span>가입완료</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data:() => ({
    isActive:{
      signUp: ["on", "none", "none", "none"],
      agree: ["none", "on", "none", "none"],
      info: ["none", "none", "on", "none"],
      complete: ["none", "none", "none", "on"],
    }
  }),
}
</script>

<style lang="scss" scoped>
.tab-wrap{
  width: 100%;
  height: 113px;
  text-align: center;
  border-top: 1px solid #000;
  border-bottom: 1px solid #000;

  .join-tab{
    width: 23%;
    max-width: 180px;
    height: 100%;
    font-size: 13px;
    font-family: "Spoqa Han Sans";
    color: #a1a1a1;
    display: inline-block;
    padding: 14px 0 14px 0;

    img{
      width: 60px;
      opacity: 0.4;
    }

    .join-tab-flex{
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
  }
  .on{
    color: #000;
    border-right: 1px solid #000;
    border-left: 1px solid #000;

    img{
      opacity: 1;
    }
  }
}

@media screen and (max-width: 400px){
  .tab-wrap {
    height: 103px;

    .join-tab{
      width: 24%;
      padding: 20px 0 3px 0;

      img{
        width: 40px;
      }

      span{
        font-size: 13px;
      }
    }

    .on{
      &:first-child{
        border-left: none;
      }

      &:last-child{
        border-right: none;
      }
    }
  }
}
</style>