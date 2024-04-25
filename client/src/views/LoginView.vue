<template>
    <v-container>
        <div class="centered" style="margin-top: 15%;">
            <div style="font-size: 24px;">
                <h2 style="margin-bottom: 15px;">Вход</h2>
                <strong><p>Логин:</p></strong>
                <input style="margin-top: 5px; border: 1px solid; text-indent: 7px;" v-model="login" placeholder="Введите логин" />
                <p style="margin-top: 10px;"></p>
                <strong><p>Пароль:</p></strong>
                <input style="margin-top: 5px; border: 1px solid; text-indent: 7px;" v-model="password" placeholder="Введите пароль" />
                <p style="margin-top: 15px;"></p>
                <button v-on:click="loginClick" style="margin-top: 15px; border: 1px solid; background-color: aqua; width: 40%;">Вход</button>
                <br />
            </div>
        </div>
    </v-container>
</template>

<script>
    import { ref } from 'vue'

    export default {
        methods: {
            loginClick() {
                alert('Привет, ' + this.login + '!');
                
            }
        },
        data () {
            return {
                login:'',
                password:''
            }
        }
    }
</script>

<style>
.centered {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
  
  