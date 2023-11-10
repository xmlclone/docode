<script setup>

import { ref } from 'vue';

const message = ref("message")
function change_message() {
    if (message.value == "message") {
        message.value = "new message"
    } else {
        message.value = "message"
    }
}

const htmlMsg = "<span style='color: red'>This is html.</span>"

const vbindtest = ref("color:red")
const vbindbool = ref(false)
const vbindobject = {
    id: "id1",
    class: "class1"
}
function change_vbindtest(){
    if (vbindtest.value == "color:red") {
        vbindtest.value = "color:blue"
    } else {
        vbindtest.value = "color:red"
    }
    vbindbool.value = vbindbool.value ? false : true
    console.log(vbindbool.value)
}

</script>

<template>

    <h1>{{ message }}</h1>

    <p>{{ 1 + 1 }}</p>

    <!-- v-on:submit.prevent="onSubmit" -->
    <!-- v-on是指令，submit是参数(部分指令可能没有参数，也可能是动态参数，动态参数使用[]，部分指令还支持缩写) -->
    <!-- prevent是修饰符，表示一些特殊的绑定方式，onSubmit就是值 -->

    <!-- v-on 缩写为@， v-bind缩写为:，动态参数缩写为 @[attr]  :[attr] -->
    <button @click="change_message()">click me change message!</button>
    <p v-bind:style="vbindtest">This is v-bind demo.</p>
    <p :style="vbindtest">This is v-bind short demo.</p>
    <button :disabled="vbindbool">look me!</button>
    <div v-bind="vbindobject">可以直接绑定对象，也就是id=xxx, class=xxx</div>
    <button @click="change_vbindtest()">click me change color!</button>

    <p>{{ htmlMsg }}</p>
    <p v-html="htmlMsg"></p>

    <!-- v-if是移除和插入元素，不是隐藏和显示 -->
    <p v-if="vbindbool">This is v-if</p>

</template>