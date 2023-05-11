const supertest = require('supertest');
const env = require('dotenv').config();

const request = supertest(process.env.BASE_URL)
const createUser = (user,job) => request.post(`/api/users/`)
    .set('accept', 'application/json')
    .send({
        "name": user,
        "job": job
    });


module.exports = {createUser}