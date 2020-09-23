<template>
  <div id="app">   	 
    <div id="page-container">
      <div id="content-wrap">
        <Header/>
      </div>
      <Body/>
      <Footer/>
    </div>
  </div>
</template>

<script>

import Header from './components/Header';
import Body from './components/Body';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    Header,
    Body,
    Footer
  }
}
</script>

<style>
* {
	padding: 0;
	margin: 0;
	box-sizing: border-box;
	font-family: 'Roboto',"Helvetica Neue", Helvetica, Arial sans-serif;
}

#page-container {
  position: relative;
  min-height: 100vh;
}

#content-wrap {
  padding-bottom: 2.5rem;    /* Footer height */
}

</style>
