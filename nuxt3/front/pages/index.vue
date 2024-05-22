<!-- pages/index.vue -->
<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Nurse Call Data</v-card-title>
          <v-card-subtitle v-if="!data.length" class="text-gray-500">Loading data...</v-card-subtitle>
          <v-data-table :headers="headers" :items="data" v-if="data.length"></v-data-table>
          <v-btn @click="addData" class="mt-4" color="primary">Add Data</v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import axios from 'axios';

const data = ref([]);
const headers = [
  { text: 'Call ID', value: 'id' },
  { text: 'Room No', value: 'room_no' },
  { text: 'Status', value: 'status' },
  { text: 'Creation Time', value: 'creation_time' },
  { text: 'Update Time', value: 'update_time' },
];

const fetchData = async () => {
  console.log('Fetching data...');
  try {
    const response = await axios.post('http://172.34.0.7:8080/select-tables/', { room: '101' });
    console.log('Data fetched:', response.data.data);
    data.value = response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

onMounted(() => {
  fetchData();
  const intervalId = setInterval(fetchData, 1000); // 1秒ごとにデータを再取得

  // コンポーネントが破棄されるときにインターバルをクリア
  onBeforeUnmount(() => {
    clearInterval(intervalId);
  });
});

const addData = async () => {
  try {
    console.log('Adding data...');
    const newEntry = {
      room: '101'
    };
    await axios.post('http://172.34.0.7:8080/add-room/', newEntry);
    // データを再取得して更新する
    fetchData();
  } catch (error) {
    console.error('Error adding data:', error);
  }
};
</script>

<style scoped>
/* カスタムCSSが必要な場合はここに追加 */
</style>
