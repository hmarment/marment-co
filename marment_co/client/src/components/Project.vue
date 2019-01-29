<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Projects</h1>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">ID</th>
              <th scope="col">Name</th>
              <th scope="col">Description</th>
              <th scope="col">Programming Language</th>
              <th scope="col">Homepage</th>
              <th scope="col">Created</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(project, index) in projects" :key="index">
              <td>{{ project.id }}</td>
              <td>{{ project.name }}</td>
              <td>{{ project.description }}</td>
              <td>{{ project.language }}</td>
              <td>{{ project.homepage }}</td>
              <td>{{ project.created_at }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      projects: [],
    };
  },
  methods: {
    getProjects() {
      const path = `${process.env.HOST}/api/github/list`;
      axios.get(path)
        .then((res) => {
          this.projects = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getProjects();
  },
};
</script>
