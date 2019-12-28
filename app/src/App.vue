<template>
  <v-app>
    <v-content>
      <MonteSeuPC/>
    </v-content>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld';
import MonteSeuPC from './components/MonteSeuPC';

export default {
  name: 'App',

  components: {
    // HelloWorld,
    MonteSeuPC,
  },

  data: () => ({
    //
  }),
};
</script>
