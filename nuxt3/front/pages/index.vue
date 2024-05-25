<template>
  <v-container>
    <v-row>
      <v-col>
        <v-card>
          <v-card-title>Nurse Call Table</v-card-title>
          <v-card-subtitle v-if="!data.length" class="text-gray-500">Loading data...</v-card-subtitle>
          <v-data-table
            dense
            :headers="headers"
            :items="data"
            class="elevation-1"
            :search="search"
            :sort-by.sync="sortBy"
            :sort-desc.sync="sortDesc"
          >
            <template v-slot:top>
              <v-text-field
                v-model="search"
                label="Search (UPPER CASE ONLY)"
                class="mx-4"
              ></v-text-field>
            </template>

            <template v-slot:[`item.status`]="{ item }">
              <v-chip
                :color="getStatusColor(item.status)"
                dark
              >
                {{ item.status }}
              </v-chip>
            </template>

            <template v-slot:[`item.actions`]="{ item }">
              <v-btn :color="getButton1Color(item.status)" class="mr-4" @click="handleButtonClick(item.id, item.status)">
                <template v-if="item.status === 'ready'">START</template>
                <template v-else-if="item.status === 'work'">DONE</template>
                <template v-else-if="item.status === 'done'">RESET</template>
              </v-btn>
              <v-btn :color="getResetButtonColor()" class="mr-4" @click="updateStatusToReady(item.id)">RESET</v-btn>
            </template>
          </v-data-table>
          <v-btn @click="addData" class="mt-4" color="primary">Add Data</v-btn>
          <v-btn @click="clearData" class="mt-4" color="primary">Clear Data</v-btn>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import axios from 'axios';

const data = ref([]);
const search = ref('');
const sortBy = ref([]);
const sortDesc = ref([]);

const headers = [
  { title: 'ID', key: 'id', sortable: true },
  { title: 'Room No', key: 'room_no', sortable: true },
  { title: 'Status', key: 'status', sortable: true },
  { title: 'Actions', key: 'actions', sortable: false }
];

const toggleSort = (column) => {
  const index = sortBy.value.indexOf(column);
  if (index === -1) {
    sortBy.value = [column];
    sortDesc.value = [false];
  } else {
    sortDesc.value = [!sortDesc.value[0]];
  }
};

const getBaseURL = () => {
  const hostname = window.location.hostname;
  if (/^192\./.test(hostname)) {
    return `${window.location.protocol}//${hostname}:8080`;
  } else if (/^172\./.test(hostname)) {
    return `${window.location.protocol}//172.34.0.7:8080}`;
  } else {
    return `${window.location.origin}`;
  }
};

const fetchData = async () => {
  const baseURL = getBaseURL();
  console.log('Fetching data...');
  try {
    const response = await axios.post(`${baseURL}/select-tables/`, { room: '101' });
    console.log('Data fetched:', response.data.data);
    data.value = response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

onMounted(() => {
  fetchData();
  const intervalId = setInterval(fetchData, 1000);

  onBeforeUnmount(() => {
    clearInterval(intervalId);
  });
});

const addData = async () => {
  const baseURL = getBaseURL();
  try {
    console.log('Adding data...');
    const newEntry = { room: '101' };
    await axios.post(`${baseURL}/add-room/`, newEntry);
    fetchData();
  } catch (error) {
    console.error('Error adding data:', error);
  }
};

const clearData = async () => {
  const baseURL = getBaseURL();
  try {
    console.log('Clearing data...');
    const newEntry = { room: '101' };
    await axios.post(`${baseURL}/update-status-to-clear/`, newEntry);
    fetchData();
  } catch (error) {
    console.error('Error clearing data:', error);
  }
};

const handleButtonClick = async (id, status) => {
  const baseURL = getBaseURL();
  try {
    console.log(`Button clicked for row with id ${id}, status ${status}`);
    const payload = { id };

    if (status === 'ready') {
      await axios.post(`${baseURL}/update-ready-to-work/`, payload);
    } else if (status === 'work') {
      await axios.post(`${baseURL}/update-work-to-done/`, payload);
    } else if (status === 'done') {
      await axios.post(`${baseURL}/update-status-to-ready/`, payload);
    }

    console.log('Data posted:', payload);
  } catch (error) {
    console.error('Error posting data:', error);
  }
};

const updateStatusToReady = async (id) => {
  const baseURL = getBaseURL();
  try {
    console.log(`Button clicked for row with id ${id}`);
    const payload = { id };
    await axios.post(`${baseURL}/update-status-to-ready/`, payload);
    console.log('Data posted:', payload);
  } catch (error) {
    console.error('Error posting data:', error);
  }
};

const getButton1Label = (status) => {
  switch (status) {
    case 'ready':
      return 'START';
    case 'work':
      return 'DONE';
    case 'done':
      return 'RESET';
    default:
      return 'ACTION';
  }
};

const getButton1Color = (status) => {
  switch (status) {
    case 'ready':
      return 'orange';
    case 'work':
      return 'green';
    case 'done':
      return 'white';
    default:
      return 'default';
  }
};

const getResetButtonColor = () => {
  return 'white';
};

const getStatusColor = (status) => {
  switch (status) {
    case 'ready':
      return 'red';
    case 'work':
      return 'green';
    default:
      return '';
  }
};
</script>

<style scoped>
.v-container {
  padding: 20px;
}

.v-btn {
  margin-right: 16px;
  color: black;
}

.v-icon.active {
  color: #42b983;
}

.d-flex {
  display: flex;
  align-items: center;
}
</style>
