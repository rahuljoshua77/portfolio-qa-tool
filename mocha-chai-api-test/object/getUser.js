const supertest = require('supertest');
const env = require('dotenv').config();

const request = supertest(process.env.BASE_URL)
const getUser = (id) => request.get(`/api/users/${id}`)
    .set('accept', 'application/json')
    .send();


module.exports = {getUser}