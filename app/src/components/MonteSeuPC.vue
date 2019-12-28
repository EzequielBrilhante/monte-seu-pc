<template >
  <div>
    <v-app-bar color="#40d0bb" dark>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

      <v-toolbar-title>Monte seu Computador</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-menu left bottom></v-menu>
    </v-app-bar>
    <br>
    <v-container>
      <!-- <v-layout> -->
      <!-- {{ placa_mae_item }} -->
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-autocomplete
          v-model="montar.placa_mae"
          :items="placa_mae_item"
          item-value="produto"
          item-text="produto"
          :rules="[v => !!v || 'Por favor, escolha um item']"
          label="Placa Mãe"
          no-data-text="Nenhuma placa mãe encontrada"
          required
        ></v-autocomplete> 
        <v-autocomplete
          v-model="montar.processador"
          :items="processador_item"
          item-value="produto"
          item-text="produto"
          :rules="[v => !!v || 'Por favor, escolha um item']"
          label="Processador"
          no-data-text="Nenhum processador encontrada"
          required
        ></v-autocomplete>
        <v-autocomplete
          v-model="montar.memoria"
          :items="memoria_item"
          item-value="produto"
          item-text="produto"
          :rules="[v => !!v || 'Por favor, escolha um item']"
          label="Memoria"
          no-data-text="Nenhuma memoria encontrada"
          required
        ></v-autocomplete>
        <v-autocomplete
          v-model="montar.tamanho_da_memoria"
          :items="tamanho_de_memoria_item"
          item-value="produto"
          item-text="produto"
          :rules="[v => !!v || 'Por favor, escolha um item']"
          label="Tamanho da Memoria"
          required
        ></v-autocomplete>
        <v-text-field
          v-model="montar.qtd_de_memoria"
          :counter="2"
          type="number"
          :rules="qtdRules"
          label="Quantidade de mémoria"
          required
        ></v-text-field>
        <v-autocomplete
          v-model="montar.placa_de_video"
          :items="placa_de_video_item"
          item-value="produto"
          item-text="produto"
          label="Placa de vídeo"
          no-data-text="Nenhuma placa de video encontrada"
        ></v-autocomplete>
        <br>
        <br>
        <br>
        <v-btn color="#40d0bb" class="mr-4" @click="reset">
          Limpar Formulario
        </v-btn>
        <v-btn
          :disabled="!valid"
          color="#40d0bb"
          class="mr-4"
          @click="montar_pc(montar)"
        >
          Enviar
        </v-btn>

      </v-form>

      <!-- </v-layout> -->
    </v-container>
  </div>
</template>

<script>
import swal from "sweetalert"
import axios from "axios"


export default {
  name: "MonteSeuPC",

  data: () => ({
    valid: true,
    processador_item : null,
    placa_de_video_item :null,
    placa_mae_item: null,
    memoria_item: null,
    montar: {
      processador: null,
      placa_mae: null,
      memoria: null,
      placa_de_video: null,
      qtd_de_memoria: null
    },
    numberRules: [v => !!v || "Você precisa digitar a quantidade de memoria"],
    tamanho_de_memoria_item: ["4GB", "8GB", "16GB", "32GB", "64GB"]
  }),
  watch:{
      "montar.placa_de_video":function(){
        if (this.montar.placa_de_video=='(Nenhuma)'){
            this.montar.placa_de_video = null
        }
      }
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/api/processadores/", {
      headers: {
        Authorization: "Token 8b361dc692375366a63487745493133a138e4d4b"
      }
    }).then(response => (this.processador_item = response.data)),

    axios.get("http://127.0.0.1:8000/api/placamaes/", {
      headers: {
        Authorization: "Token 8b361dc692375366a63487745493133a138e4d4b"
      }
    }).then(response => (this.placa_mae_item = response.data)),

    axios.get("http://127.0.0.1:8000/api/memorias/", {
      headers: {
        Authorization: "Token 8b361dc692375366a63487745493133a138e4d4b"
      }
    }).then(response => (this.memoria_item = response.data)),

    axios.get("http://127.0.0.1:8000/api/placasdevideo/", {
      headers: {
        Authorization: "Token 8b361dc692375366a63487745493133a138e4d4b"
      }
    }).then(response => {
      this.placa_de_video_item = response.data
      this.placa_de_video_item.unshift({
          "produto":"(Nenhuma)"
      })
    });
  },
  methods: {
    montar_pc(montar) {
      axios.post("http://127.0.0.1:8000/api/monteseupc/", montar, {
        headers: {
          Authorization: "Token 8b361dc692375366a63487745493133a138e4d4b"
        }
      }).then(response => {
        if (response.status == 201) {
          swal({
            title: "Pedido Realizado com Sucesso",
            icon: "success",
            button: "OK"
          });
        }
      }).catch(function(error) {
        if (error.response.status != 201) {
          swal({
            title: "Erro ao realizar pedido",
            text: error.response.data.non_field_errors[0],
            icon: "error",
            button: "OK"
          });
        }
      });
    },
    reset() {
      this.$refs.form.reset();
    }
  }
};
</script>


<style>
.swal-text{
  font-weight:600;
  text-align: center;
  text-transform: capitalize;
}
.container-form-max{
    max-width: 900px;
}
</style>